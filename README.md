# Data Mining Group Project: Recommender System
## Links
- [Video Report](https://youtu.be/JGu9R1OfJJ4)
- [Presentation Slides](https://docs.google.com/presentation/d/1-Jgbv7lyp4KOXJcu_9RxMHoH6h5NrO-Uhh0CArOElRs/edit?usp=sharing)(though I'm absolutely sure you won't need it)


## Developers info

### Data collection and preparation
#### MovieLens 1M
`python src/datasets/download_movie_lens.py` - downloading MovieLens 1M dataset  
`python src/datasets/merge_movie_lens.py` - preprocessing and merging MovieLens dataset

#### IMDB
`python src/datasets/download_imdb.py` - downloading IMDB dataset

#### Combination
To match titles in the movielens dataset and ids in imdb dataset, you should run
```
python src/datasets/extract_movielens_to_imdb_mapping.py
```  
This creates `data/movielens_to_imdb_mapping.csv` file. For now, the script gives 
~3000/3700 matches. The script may take ~10 minutes, so I suggest to use the 
existing matching file in from the repo.  
After it, to extract IMDB features, run
```
python src/datasets/augment_movielens.py
```  
The current version extracts average rating of the film and number of votes.

