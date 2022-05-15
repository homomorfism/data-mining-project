import pandas as pd
import os
import logging
from argparse import ArgumentParser
from typing import Optional
from utils import decode_string


def merge_movie_lens(
    root: Optional[str] = "data/movie_lens/ml-1m",
    out: Optional[str] = "data/movie_lens/movie_lens_1m.csv"
) -> None:
    movies_file_path = os.path.join(root, "movies.dat")
    ratings_file_path = os.path.join(root, "ratings.dat")
    users_file_path = os.path.join(root, "users.dat")

    # Converting movies file to .csv format
    logging.info("Converting movies file to .csv format...")
    movies_dict = {
        "MovieID": list(),
        "Title": list(),
        "Genres": list()
    }
    with open(movies_file_path, "rb") as f:
        while True:
            line = f.readline()
            if line:
                line = decode_string(line)
                line = line.replace("\n", "")
                movie_id, title, genres = line.split("::")
                movie_id = int(movie_id)
                movies_dict["MovieID"].append(movie_id)
                movies_dict["Title"].append(title)
                movies_dict["Genres"].append(genres)
            else:
                break

    movies_df = pd.DataFrame.from_dict(movies_dict)

    # Converting ratings file to .csv format
    logging.info("Converting ratings file to .csv format...")
    ratings_dict = {
        "UserID": list(),
        "MovieID": list(),
        "Rating": list(),
        "Timestamp": list()
    }
    with open(ratings_file_path, "rb") as f:
        while True:
            line = f.readline()
            if line:
                line = decode_string(line)
                line = line.replace("\n", "")
                user_id, movie_id, rating, timestamp = line.split("::")
                user_id = int(user_id)
                movie_id = int(movie_id)
                ratings_dict["UserID"].append(user_id)
                ratings_dict["MovieID"].append(movie_id)
                ratings_dict["Rating"].append(rating)
                ratings_dict["Timestamp"].append(timestamp)
            else:
                break

    ratings_df = pd.DataFrame.from_dict(ratings_dict)

    # Converting users file to .csv format
    logging.info("Converting users file to .csv format...")
    users_dict = {
        "UserID": list(),
        "Gender": list(),
        "Age": list(),
        "Occupation": list(),
        "ZipCode": list()
    }
    with open(users_file_path, "rb") as f:
        while True:
            line = f.readline()
            if line:
                line = decode_string(line)
                line = line.replace("\n", "")
                user_id, gender, age, occupation, zip_code = line.split("::")
                user_id = int(user_id)
                age = int(age)
                occupation = int(occupation)
                users_dict["UserID"].append(user_id)
                users_dict["Gender"].append(gender)
                users_dict["Age"].append(age)
                users_dict["Occupation"].append(occupation)
                users_dict["ZipCode"].append(zip_code)
            else:
                break

    users_df = pd.DataFrame.from_dict(users_dict)

    # Merging the dataframes
    logging.info("Merging the dataframes...")
    ratings_with_movies_df = ratings_df.merge(movies_df, on="MovieID", how="left")
    merged_df = ratings_with_movies_df.merge(users_df, on="UserID", how="left")

    merged_df.to_csv(out, index=False)
    logging.info("Data is ready.")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--root", "-r", type=str, default="data/movie_lens/ml-1m/", help="Data root directory")
    parser.add_argument(
        "--out",
        "-o",
        type=str,
        default="data/movie_lens/movie_lens_1m.csv",
        help="Path to the .csv file with merged data"
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    merge_movie_lens(args.root, args.out)
