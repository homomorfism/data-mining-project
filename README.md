# [S22]. Data Mining. Group Project

## Data collection and preparation
### MovieLens 1M
`python src/datasets/download_movie_lens.py` - downloading MovieLens 1M dataset  
`python src/datasets/merge_movie_lens.py` - preprocessing and merging MovieLens dataset

### IMDB
`python src/datasets/download_imdb.py` - downloading IMDB dataset

### Combination
To match titles in the movielens dataset and ids in imdb dataset, you should run
```python src/datasets/extract_movielens_to_imdb_mapping.py```  
This creates `data/movielens_to_imdb_mapping.csv` file. For now, the script gives 
~3000/3700 matches. The script may take ~10 minutes, so I suggest to use the 
existing matching file in from the repo.
