# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details['amenities_count'] = airbnb_search_details['amenities'].str.count(',') + 1

cities = airbnb_search_details.groupby('city', as_index = False).agg(total_amenities = ('amenities_count', 'sum')).sort_values(by = 'total_amenities', ascending = False)

cities['city'].head(1)
