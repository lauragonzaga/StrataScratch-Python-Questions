# Import your libraries
import pandas as pd

merged = worker.merge(title, left_on = 'worker_id', right_on = 'worker_ref_id')

highest_salary = merged['salary'].max()

merged[merged['salary'] == highest_salary]['worker_title']
