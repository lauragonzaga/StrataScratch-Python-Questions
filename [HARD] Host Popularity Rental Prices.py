# Import your libraries
import pandas as pd

airbnb_host_searches['host_id'] = airbnb_host_searches['price'].map(str) + airbnb_host_searches['room_type'].map(str) + airbnb_host_searches['host_since'].map(str) +airbnb_host_searches['zipcode'].map(str) + airbnb_host_searches['number_of_reviews'].map(str)

df = airbnb_host_searches[['host_id', 'price', 'number_of_reviews']].drop_duplicates()


def rating(x):
    if x == 0:
        return 'new'
    elif 0 < x <= 5:
        return 'rising'
    elif 6 <= x <= 15:
        return 'trending up'
    elif 16 <= x <= 40:
        return 'popular'
    else:
        return 'hot'

df['popularity'] = df['number_of_reviews'].apply(rating)

df.groupby('popularity').agg(min_price=('price',min),avg_price = ('price','mean'),max_price = ('price',max)).reset_index()
