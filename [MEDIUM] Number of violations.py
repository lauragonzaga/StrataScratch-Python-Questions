# Import your libraries
import pandas as pd

# Start writing code
roxanne_cafe = sf_restaurant_health_violations[sf_restaurant_health_violations['business_name'] == 'Roxanne Cafe']

roxanne_cafe['year'] = roxanne_cafe['inspection_date'].dt.year

roxanne_cafe.groupby('year')['violation_id'].count().to_frame('n_violations').reset_index()
