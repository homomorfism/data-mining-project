import gzip
import shutil
from pathlib import Path

from utils import download

imdb_links = [
    'https://datasets.imdbws.com/name.basics.tsv.gz',
    'https://datasets.imdbws.com/title.akas.tsv.gz', 
    'https://datasets.imdbws.com/title.basics.tsv.gz', 
    'https://datasets.imdbws.com/title.crew.tsv.gz', 
    'https://datasets.imdbws.com/title.episode.tsv.gz', 
    'https://datasets.imdbws.com/title.principals.tsv.gz', 
    'https://datasets.imdbws.com/title.ratings.tsv.gz', 
]

def load_imdb_datasets():
    datadir = Path('data/imdb')
    datadir.mkdir(parents=True, exist_ok=True)

    filenames = [link.split('/')[-1] for link in imdb_links]
    for filename, url in zip(filenames, imdb_links):
        filepath = datadir / filename
        print(f'Downloading {url}')
        download(url, filepath)
        print(f'Decompressing...', end=' ')
        decompress_gz_file(filepath)
        print(f'Removing...')
        filepath.unlink() # this is remove operation



def decompress_gz_file(filepath):
    assert filepath.suffix == '.gz', "Expected .gz file while loading IMDB dataset"
    unzipped_filepath = filepath.with_suffix('')
    with gzip.open(filepath, 'rb') as f_in:
        with open(unzipped_filepath, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            

if __name__ == '__main__':
    load_imdb_datasets()
