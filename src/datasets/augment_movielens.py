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


def augment_with_genres(movielens: pd.DataFrame) -> pd.DataFrame:
    genres = set(it.chain(*movielens.Genres.apply(lambda x: x.split("|"))))
    genre_columns = [f"is{genre}Movie" for genre in genres]
    genre_bitmasks = list(movielens.Genres.apply(encode_ohe_genre, args=[genres]))
    movielens[genre_columns] = genre_bitmasks
    del movielens['Genres']
    return movielens

def encode_ohe_genre(genre_str: str, all_genres: set) -> list:
    title_genres = set(genre_str.split("|"))
    bitmask_genres = [genre in title_genres for genre in all_genres]
    return bitmask_genres


if __name__ == '__main__':
    movielens = pd.read_csv("data/movie_lens/movie_lens_1m.csv")
    augmented_movielens = augment_with_ratings(movielens)
    augmented_movielens = augment_with_genres(augmented_movielens)
    augmented_movielens.to_csv("data/augmented_movie_lens.csv", index=False)

