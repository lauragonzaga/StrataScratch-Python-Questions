# Import your libraries
import pandas as pd

# Start writing code
monthly_revenue = sf_transactions.groupby(sf_transactions['created_at'].dt.to_period('M')).agg(revenue = ('value', 'sum')).reset_index().rename(columns = {'created_at': 'month'})

monthly_revenue['previous_revenue'] = monthly_revenue['revenue'].shift(1)

monthly_revenue['percentage'] = (monthly_revenue['revenue'] - monthly_revenue['previous_revenue']) / monthly_revenue['previous_revenue'] * 100

monthly_revenue[['month', 'percentage']]
