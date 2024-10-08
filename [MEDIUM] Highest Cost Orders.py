# Import your libraries
import pandas as pd


merged = customers.merge(orders, how = 'right', left_on = 'id', right_on = 'cust_id')

merged = merged[(merged['order_date'] >= '2019-02-01') & (merged['order_date'] <= '2019-05-01')]

order_cost_sum = merged.groupby(['first_name', 'order_date']).agg(total_cust_cost = ('total_order_cost', 'sum')).reset_index()

order_cost_sum.sort_values('total_cust_cost', ascending = False).head(1)
