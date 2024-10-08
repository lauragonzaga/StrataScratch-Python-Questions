# Import your libraries
import pandas as pd

# Start writing code
merged = amazon_transactions.merge(amazon_transactions, how = 'left', on = 'user_id').drop_duplicates()

active_users = merged[((merged['created_at_y'] - merged['created_at_x']).dt.days <= 7) &
        ((merged['created_at_y'] - merged['created_at_x']).dt.days >= 0) &
        (merged['id_x'] != merged['id_y'])].sort_values('user_id')



active_users['user_id'].unique()
