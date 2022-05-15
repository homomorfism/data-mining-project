import pandas as pd


class ImdbSearcher:
    def __init__(self, database: pd.DataFrame):
        self.imdb = database
        
    def get_by_name_and_year(self, title_name: str, year: str) -> pd.Series:
        candidates = self._search_imdb(title_name, year)
        if len(candidates) == 0:
            return None 
        else:
            return candidates.iloc[0].tconst
        
    def _search_imdb(self, title_name: str, year: str) -> pd.Series:
        candidates = self.imdb.query("originalTitle == @title_name and startYear == @year")
        return candidates
    
    def _test_n_candidates_is_one(self, candidate: pd.DataFrame, title_name: str):
        if len(candidate) > 1:
            raise Exception(f"Too much found for title name {title_name}")
        if len(candidate) == 0:
            raise Exception(f"Nothing found for title name {title_name}")
