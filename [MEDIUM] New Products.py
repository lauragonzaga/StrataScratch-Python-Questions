# Import your libraries
import pandas as pd

new_products = car_launches .groupby(['year','company_name']).agg(products_count = ('product_name', 'count')).reset_index()


new_products_2019 = new_products[new_products['year'] == 2019]

new_products_2020 = new_products[new_products['year'] == 2020]


merged = new_products_2019.merge(new_products_2020, on = 'company_name')


merged['net_new_products'] = merged['products_count_y'] - merged['products_count_x']

merged[['company_name', 'net_new_products']]
