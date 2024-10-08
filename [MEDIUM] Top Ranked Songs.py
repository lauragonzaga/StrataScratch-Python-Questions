# Import your libraries
import pandas as pd

# Start writing code
spotify_worldwide_daily_song_ranking[spotify_worldwide_daily_song_ranking['position'] == 1].groupby('trackname').agg(times_top1 = ('trackname', 'count')).reset_index().sort_values('times_top1', ascending = False)
