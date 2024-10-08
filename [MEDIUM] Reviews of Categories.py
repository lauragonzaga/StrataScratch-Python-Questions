# Import your libraries
import pandas as pd

# Start writing code


##

yelp_business['categories'] = yelp_business['categories'].str.split(';')

yelp_business = yelp_business.explode('categories')

yelp_business.groupby('categories').agg(total_reviews = ('review_count', 'sum')).reset_index().sort_values(by = 'total_reviews', ascending = False)
