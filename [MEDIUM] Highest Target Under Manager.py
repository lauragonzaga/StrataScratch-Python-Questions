# Import your libraries
import pandas as pd

# Start writing code
manager_13 = salesforce_employees[salesforce_employees['manager_id'] == 13]

highest_target = manager_13[manager_13['target'] == manager_13['target'].max()]

highest_target[['first_name', 'target']]
