# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = None

# -

upstream = ['get']

product = 'products/clean.csv'

import pandas as pd

df = pd.read_csv('products/raw.csv', index_col=0)

df.columns = ['Columna 1', 'Columna 2']

df.to_csv(product)
