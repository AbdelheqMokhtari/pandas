import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Use .loc for filtering and avoid creating intermediate DataFrames
    results = world.loc[(world["2022 Population"] >= 25000000) | (world["Area (km²)"] >= 3000000), ["Country/Territory",
                                                                                                    "2022 Population",
                                                                                                    "Area (km²)"]]
    return results


countries = pd.read_csv('world_population.csv')
print(big_countries(countries))