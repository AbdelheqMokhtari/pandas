import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    results = views.loc[views['author_id'] == views['viewer_id'],['author_id']]
    results.rename(columns={"author_id": "id"}, inplace=True)
    results = results.sort_values(by ='id')
    return results.drop_duplicates(keep='first')