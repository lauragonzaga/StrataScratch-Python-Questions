# Import your libraries
import pandas as pd

# Start writing code
fraud_score['percentile'] = fraud_score.groupby('state')['fraud_score'].rank(pct = True)

top_five = fraud_score[fraud_score['percentile'] > 0.95]

top_five[['policy_num', 'state', 'claim_cost', 'fraud_score']]
