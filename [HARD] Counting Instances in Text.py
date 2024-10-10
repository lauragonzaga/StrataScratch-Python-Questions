# Import your libraries
import pandas as pd
import re

# Start writing code
gfs = google_file_store

gfs['bull'] = gfs['contents'].str.count(r'\bbull\b', flags = re.I)

gfs['bear'] = gfs['contents'].str.count(r'\bbear\b', flags = re.I)

gfs[['bull', 'bear']].sum().reset_index('word')
