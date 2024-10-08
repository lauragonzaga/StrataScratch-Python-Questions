# Import your libraries
import pandas as pd

airbnb_hosts = airbnb_hosts.drop_duplicates()

merged = airbnb_hosts.merge(airbnb_units, how = 'right', on = 'host_id')

under_30 = merged[(merged['age'] < 30) & (merged['unit_type']=='Apartment')]

under_30.groupby('nationality').agg(apartment_count = ('unit_id', 'count')).reset_index().sort_values(by = 'apartment_count', ascending = False)
