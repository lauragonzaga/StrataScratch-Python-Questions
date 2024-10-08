# Import your libraries
import pandas as pd

pairs = airbnb_hosts.merge(airbnb_guests, how = 'left', on = ['gender', 'nationality'])

pairs[['host_id', 'guest_id']].drop_duplicates()
