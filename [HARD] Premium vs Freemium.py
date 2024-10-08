# Import your libraries
import pandas as pd

# Merge as dimensões
merged_1 = ms_user_dimension.merge(ms_acc_dimension, on='acc_id').merge(ms_download_facts, on='user_id')

# Usar pivot_table para agregar downloads por data e tipo de cliente
final_df = merged_1.pivot_table(
    index='date',
    columns='paying_customer',
    values='downloads',
    aggfunc='sum',
    fill_value=0  # Substitui NaNs por 0
).reset_index()

final_df[final_df['no'] > final_df['yes']]
