# Import your libraries
import pandas as pd

sent = fb_friend_requests[fb_friend_requests['action'] == 'sent']

accepted = fb_friend_requests[fb_friend_requests['action'] == 'accepted']

requests = sent.merge(accepted, how = 'outer', on = 'user_id_receiver')


requests = requests.groupby('date_x').agg(total_requests = ('action_x', 'count'), accepted_requests = ('action_y', 'count')).reset_index()

requests['acceptance_rate'] = requests ['accepted_requests'] / requests['total_requests'] 

requests[['date_x', 'acceptance_rate']]
