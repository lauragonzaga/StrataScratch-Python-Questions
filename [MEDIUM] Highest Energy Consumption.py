# Import your libraries
import pandas as pd

# Start writing code
total_consumption = pd.concat([fb_eu_energy, fb_asia_energy, fb_na_energy]).groupby('date').agg(total_consumption = ('consumption','sum')).reset_index()

total_consumption[total_consumption['total_consumption'] == (total_consumption['total_consumption'].max())]
