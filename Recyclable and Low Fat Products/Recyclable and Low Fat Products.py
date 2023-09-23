import numpy as np
import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'), ['product_id']]


# Constructing DataFrame from a dictionary.
data = {'product_id': [0, 1, 2, 3, 4], 'low_fats': ['Y', 'Y', 'N', 'Y', 'N'], 'recyclable': ['N', 'Y', 'Y', 'Y', 'N']}
df = pd.DataFrame(data=data)

print(find_products(df))

