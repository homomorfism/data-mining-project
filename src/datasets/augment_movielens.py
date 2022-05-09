import itertools as it
import pandas as pd
import numpy as np

def augment_with_ratings(movielens: pd.DataFrame) -> pd.DataFrame:
    ratings = pd.read_csv("data/imdb/title.ratings.tsv", sep='\t').set_index("tconst")
    matching = pd.read_csv("data/movielens_to_imdb_mapping.csv").set_index("title")
    movielens_ratings = matching.join(ratings, on='tconst')
    movielens_ratings['logNumVotes'] = np.log(movielens_ratings.numVotes)
    del movielens_ratings['numVotes']
    del movielens_ratings['tconst']
    movielens_ratings
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


if __name__ == '__main__':
    movielens = pd.read_csv("data/movie_lens/movie_lens_1m.csv")
    augmented_movielens = augment_with_ratings(movielens)
    augmented_movielens = encode_bitmask_genres(augmented_movielens)
    augmented_movielens = encode_ohe_age(augmented_movielens)
    augmented_movielens = encode_ohe_occupation(augmented_movielens)
    augmented_movielens = process_gender(augmented_movielens)
    augmented_movielens.to_csv("data/augmented_movie_lens.csv", index=False)

