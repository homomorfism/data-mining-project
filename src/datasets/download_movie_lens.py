import wget
import os
import logging
from argparse import ArgumentParser
from zipfile import ZipFile


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--url",
        "-u",
        type=str,
        default="https://files.grouplens.org/datasets/movielens/ml-1m.zip",
        help="URL of the file to download"
    )
    parser.add_argument(
        "--save-dir",
        "-s",
        default="./data/movie_lens",
        type=str,
        help="Destination folder"
    )
    parser.add_argument("--name", "-n", default="movie_lens_1m.zip", type=str, help="Filename")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)

    os.makedirs(args.save_dir, exist_ok=True)
    logging.info("Downloading file...")
    wget.download(url=args.url, out=os.path.join(args.save_dir, args.name))
    print("\n")
    logging.info("File is downloaded, unzipping...")
    with ZipFile(os.path.join(args.save_dir, args.name), "r") as zip_f:
        zip_f.extractall(path=args.save_dir)
    logging.info("Data is unzipped.")

    os.remove(os.path.join(args.save_dir, args.name))
    logging.info(".zip file is deleted.")
