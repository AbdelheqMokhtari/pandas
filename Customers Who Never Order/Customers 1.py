import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge the customers DataFrame with the orders DataFrame using a left join on 'id' and 'customerId'
    merged_df = customers.merge(orders, how='left', left_on='id', right_on='customerId')

    # Use the 'customerId' column to create a boolean mask for customers who never placed any orders
    mask = merged_df['customerId'].isna()

    # Filter the rows using the boolean mask
    result_df = merged_df[mask]

    # Select only the 'name' column from the result DataFrame and rename it as 'Customers'
    result_df = result_df[['name']].rename(columns={'name': 'Customers'})

    return result_df


customers_list = {'id': [1, 2, 3, 4], 'name': ['Joe', 'Henry', 'Sam', 'Max']}
orders_list = {'id': [1, 2], 'customerId': [3, 1]}

customers_dataframe = pd.DataFrame(data=customers_list)
orders_dataframe = pd.DataFrame(data=orders_list)

print(find_customers(customers_dataframe, orders_dataframe))
