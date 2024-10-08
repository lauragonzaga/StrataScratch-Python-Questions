# Import your libraries
import pandas as pd

# Start writing code
user_flags = user_flags[user_flags['flag_id'].notnull()]

user_flags['user_full_name'] = user_flags['user_firstname'].astype(str) + ' ' + user_flags['user_lastname']

user_flags.groupby('video_id')['user_full_name'].nunique().reset_index().rename(columns={"user_full_name": "num_unique_users"})
