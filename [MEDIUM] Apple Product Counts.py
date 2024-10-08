# Import your libraries
import pandas as pd

# Start writing code
merged = playbook_events.merge(playbook_users, on = 'user_id')

apple_products = ['iphone 5s','macbook pro','ipad air']

apple_users = merged[merged['device'].isin(apple_products)].groupby('language')['user_id'].nunique().to_frame('n_apple_users')

all_users = merged.groupby('language')['user_id'].nunique().to_frame('n_total_users')

apple_users.merge(all_users, how = 'outer', on = 'language').fillna(0).reset_index().sort_values(['n_apple_users', 'n_total_users'], ascending = False)
