# Import your libraries
import pandas as pd

activity_rank = google_gmail_emails.groupby('from_user').agg(total_emails=('id', 'count')).reset_index()


activity_rank = activity_rank.sort_values(by = ['total_emails', 'from_user'], ascending = [False, True])


activity_rank['rank'] = activity_rank['total_emails'].rank(method = 'first', ascending=False)

activity_rank
