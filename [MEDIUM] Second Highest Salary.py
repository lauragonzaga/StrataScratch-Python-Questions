# Import your libraries
import pandas as pd

employee['ranking'] = employee['salary'].rank(method = 'dense', ascending = False)

employee = employee.sort_values(by= 'salary', ascending = False)

employee[employee['ranking'] == 2]['salary']
