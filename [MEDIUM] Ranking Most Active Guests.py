# Import your libraries
import pandas as pd

# Start writing code
active_guest_rank = airbnb_contacts.groupby('id_guest').agg(messages=('n_messages', 'sum')).reset_index().sort_values(by = 'messages', ascending = False)

active_guest_rank['ranking'] = active_guest_rank.messages.rank(method= 'dense', ascending = False)

active_guest_rank
