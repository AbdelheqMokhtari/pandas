import pandas as pd


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    results = views.loc[views['author_id'] == views['viewer_id'],['author_id']]
    results.rename(columns={"author_id": "id"}, inplace=True)
    results = results.sort_values(by='id')
    return results.drop_duplicates(keep='first')


views_table = {'article_id': [1, 1, 2, 2, 4, 3, 3],
               'author_id': [3, 3, 7, 7, 7, 4, 4],
               'viewer_id': [5, 6, 7, 6, 1, 4, 4]
               }


views_dataframe = pd.DataFrame(data=views_table)
print(article_views(views_dataframe))

