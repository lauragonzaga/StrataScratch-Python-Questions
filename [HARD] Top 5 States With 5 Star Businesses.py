# Import your libraries
import pandas as pd

# Start writing code
business_5_stars = yelp_business[yelp_business['stars'] == 5]

states = business_5_stars.groupby('state').agg(count_hotels = ('business_id', 'count')).reset_index()

states['rank'] = states['count_hotels'].rank(method = 'min', ascending = False)

states[states['rank'] <= 5].sort_values(by = 'rank')[['state', 'count_hotels']]
