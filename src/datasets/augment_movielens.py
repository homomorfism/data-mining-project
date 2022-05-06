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

if __name__ == '__main__':
    movielens = pd.read_csv("data/movie_lens/movie_lens_1m.csv")
    augmented_movielens = augment_with_ratings(movielens)
    augmented_movielens.to_csv("data/augmented_movie_lens.csv", index=False)

