# Import your libraries
import pandas as pd
import numpy as np

## overbudget = cost > budget


project_cost = linkedin_employees.merge(linkedin_emp_projects, left_on = 'id', right_on = 'emp_id', how = 'inner').groupby('project_id')['salary'].sum().reset_index()

projects = project_cost.merge(linkedin_projects, left_on = 'project_id', right_on = 'id').rename(columns = {'salary': 'cost'})

projects['days'] = (projects['end_date'] - projects['start_date']).dt.days

projects['prorated_expense'] = np.ceil(projects['cost'] / 365 * projects['days'])

projects['overbudget'] = projects['prorated_expense'] > projects['budget']

overbudget_projects = projects[projects['overbudget'] == True]

overbudget_projects[['title', 'budget', 'prorated_expense']]
