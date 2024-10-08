# Import your libraries
import pandas as pd

# Start writing code
merged = orders.merge(customers, left_on = 'cust_id', right_on = 'id')

merged['address'].count() / merged['id_x'].count() * 100
