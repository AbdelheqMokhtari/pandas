import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = pd.DataFrame()
    result['Customers'] = customers.loc[~customers['id'].isin(orders["customerId"].values),['name']]
    return result


customers_list = {'id': [1, 2, 3, 4], 'name': ['Joe', 'Henry', 'Sam', 'Max']}
orders_list = {'id': [1, 2], 'customerId': [3, 1]}

customers_dataframe = pd.DataFrame(data=customers_list)
orders_dataframe = pd.DataFrame(data=orders_list)

print(find_customers(customers_dataframe, orders_dataframe))

