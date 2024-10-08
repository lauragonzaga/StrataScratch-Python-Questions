# Import your libraries
import pandas as pd

merged = facebook_posts.merge(facebook_post_views, on = 'post_id', how = 'right')



merged['spam'] = merged['post_keywords'].str.contains('spam')


grouped = merged.groupby('post_date').agg(
        total_posts = ('post_id','count'),
        spam_posts = ('spam', 'sum')).reset_index() 
        
        
grouped['spam_share'] = grouped['spam_posts'] / grouped['total_posts'] * 100

grouped[['post_date', 'spam_share']]
