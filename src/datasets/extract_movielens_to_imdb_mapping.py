import pandas as pd
from tqdm.auto import tqdm
tqdm.pandas()

from imdb_management import ImdbSearcher


def get_tconst_by_title(title: str, searcher: ImdbSearcher) -> str:
    title_name = extract_name_from_title(title)
    title_year = extract_year_from_title(title)
    imdb_row = searcher.get_by_name_and_year(title_name, title_year)
    return imdb_row


def extract_name_from_title(title: str) -> str:
    tokens = title.split()
    title_name_tokens = tokens[:-1]
    # handles cases like "Devil's Advocate, The"
    if title_name_tokens[-1] == "The" or title_name_tokens[-1] == "A":  
        title_name_tokens.insert(0, title_name_tokens[-1])
        title_name_tokens.pop(-1)
        title_name_tokens[-1] = title_name_tokens[-1][:-1] # remove comma in last token
    title_name = ' '.join(title_name_tokens)
    return title_name

    
def extract_year_from_title(title: str) -> str:
    tokens = title.split()
    year_token = tokens[-1]
    assert year_token[0] == '(' and year_token[-1] == ')', f"Unexpected title format for string '{title}'"
    year = year_token[1:-1]
    return year


if __name__ == '__main__':
    movielens = pd.read_csv("data/movie_lens/movie_lens_1m.csv")
    imdb = pd.read_csv("data/imdb/title.basics.tsv", sep='\t')
    imdb['originalTitle'] = imdb.originalTitle.astype(str)
    imdb['startYear'] = imdb.startYear.astype(str)

    searcher = ImdbSearcher(imdb)
    title_to_imdb_id = pd.DataFrame({"title": movielens.Title.unique()})
    title_to_imdb_id['tconst'] = title_to_imdb_id.title.progress_apply(get_tconst_by_title, args=[searcher])
    title_to_imdb_id.to_csv("data/movielens_to_imdb_mapping.csv", index=False)

