import itertools as it
import pandas as pd
import numpy as np
from collections import Counter


def augment_with_ratings(movielens: pd.DataFrame) -> pd.DataFrame:
    ratings = pd.read_csv("data/imdb/title.ratings.tsv", sep='\t').set_index("tconst")
    matching = pd.read_csv("data/movielens_to_imdb_mapping.csv").set_index("title")
    movielens_ratings = matching.join(ratings, on='tconst')
    movielens_ratings['logNumVotes'] = np.log(movielens_ratings.numVotes)
    del movielens_ratings['numVotes']
    del movielens_ratings['tconst']
    movielens_ratings.rename({
        'logNumVotes': 'logNumVotesMovie',
        'averageRating': 'averageRatingMovie',
    }, axis=1, inplace=True)
    return movielens.join(movielens_ratings, on='Title')


def encode_bitmask_genres(movielens: pd.DataFrame) -> pd.DataFrame:
    genres = set(it.chain(*movielens.Genres.apply(lambda x: x.split("|"))))
    genre_columns = [f"is{genre}Movie" for genre in genres]
    genre_bitmasks = list(movielens.Genres.apply(encode_single_genre_bitmask, args=[genres]))
    movielens[genre_columns] = genre_bitmasks
    del movielens['Genres']
    return movielens


def encode_single_genre_bitmask(genre_str: str, all_genres: set) -> list:
    title_genres = set(genre_str.split("|"))
    bitmask_genres = [genre in title_genres for genre in all_genres]
    return bitmask_genres


def encode_ohe_age(movielens: pd.DataFrame) -> pd.DataFrame:
    # log of the age
    movielens["logAgeUser"] = np.log(movielens["Age"])
    # One-hot encoding the age (because there are just 7 variants there)
    unique_ages = movielens.Age.unique()
    categories = unique_ages.astype(str)
    category_columns = [f"isAge{category}User" for category in categories]
    age_bitmasks = movielens.Age.astype(str).apply(
        ohe_value, args=[categories]
    )
    movielens[category_columns] = list(age_bitmasks)
    del movielens['Age']
    return movielens


def encode_ohe_occupation(movielens: pd.DataFrame) -> pd.DataFrame:
    unique_occupations = movielens.Occupation.unique()
    categories = unique_occupations.astype(str)
    category_columns = [f"isOccupation{category}User" for category in categories]
    occupation_bitmasks = movielens.Occupation.astype(str).apply(
        ohe_value, args=[categories]
    )
    movielens[category_columns] = list(occupation_bitmasks)
    del movielens['Occupation']
    return movielens


def ohe_value(value: str, categories: set) -> list:
    ohe = [category == value for category in categories]
    return ohe


def process_gender(movielens: pd.DataFrame) -> pd.DataFrame:
    movielens['GenderUser'] = movielens.Gender == 'M'
    del movielens['Gender']
    return movielens


def add_top_directors(movielens: pd.DataFrame) -> pd.DataFrame:
    imdb_crew_data = pd.read_csv("data/imdb/title.crew.tsv", sep="\t")
    movie_lens_to_imdb_mapping = pd.read_csv("data/movielens_to_imdb_mapping.csv")

    ml_directors = movie_lens_to_imdb_mapping.merge(imdb_crew_data[["tconst", "directors"]], on="tconst", how="left")
    directors_list_raw = ml_directors["directors"].tolist()
    directors_list = list()
    for d in directors_list_raw:
        if pd.isna(d):
            continue

        ds = d.split(",")
        for director in ds:
            directors_list.append(director)

    occurrences = dict(sorted(Counter(directors_list).items(), key=lambda x: x[1], reverse=True))
    top_directors = list()
    for d, c in occurrences.items():
        if c >= 10:
            top_directors.append(d)
        else:
            break

    top_director_is_involved = list()
    for _, row in ml_directors.iterrows():
        top_flag = 0
        if not pd.isna(row["directors"]):
            directors = row["directors"].split(",")
            for d in directors:
                if d in top_directors:
                    top_flag = 1

        top_director_is_involved.append(top_flag)

    ml_directors["topDirectorMovie"] = pd.Series(top_director_is_involved)

    merged = movielens.merge(ml_directors.rename(columns={"title": "Title"}), on="Title", how="left")
    del merged["tconst"]
    del merged["directors"]

    return merged


if __name__ == '__main__':
    movielens = pd.read_csv("data/movie_lens/movie_lens_1m.csv")
    augmented_movielens = augment_with_ratings(movielens)
    augmented_movielens = encode_bitmask_genres(augmented_movielens)
    augmented_movielens = encode_ohe_age(augmented_movielens)
    augmented_movielens = encode_ohe_occupation(augmented_movielens)
    augmented_movielens = process_gender(augmented_movielens)
    augmented_movielens = add_top_directors(augmented_movielens)
    augmented_movielens.to_csv("data/augmented_movie_lens.csv", index=False)
