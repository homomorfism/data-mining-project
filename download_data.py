import wget
import os
from argparse import ArgumentParser


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--url",
        "-u",
        type=str,
        default="https://files.grouplens.org/datasets/movielens/ml-1m.zip",
        help="URL of the file to download"
    )
    parser.add_argument("--save-dir", "-s", default="./data/movielens-1m", type=str, help="Destination folder")
    args = parser.parse_args()

    os.makedirs(args.save_dir, exist_ok=True)
    wget.download(url=args.url, out=args.save_dir)
