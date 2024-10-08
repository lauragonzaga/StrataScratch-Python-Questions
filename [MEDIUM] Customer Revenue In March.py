# Import your libraries
import pandas as pd

# Start writing code
march_orders = orders[orders['order_date'].dt.month == 3]

march_orders.groupby('cust_id').agg(revenue= ('total_order_cost', 'sum')).reset_index()
