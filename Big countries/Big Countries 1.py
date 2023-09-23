import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    sort = world[["name", "2022 Population", "Area (km²)"]]
    results = sort[(sort["2022 Population"] >= 25000000) | (sort["Area (km²)"] >= 3000000)]
    return results

