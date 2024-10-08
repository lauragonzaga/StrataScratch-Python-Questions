# Import your libraries
import pandas as pd

# Start writing code


sf_bonus_summed = sf_bonus.groupby('worker_ref_id')['bonus'].sum().reset_index()


merged = sf_employee.merge(sf_bonus_summed, left_on = 'id', right_on = 'worker_ref_id')


merged['total_compensation'] = merged['salary'] + merged['bonus']


merged.groupby(['employee_title', 'sex'])['total_compensation'].mean().reset_index()
