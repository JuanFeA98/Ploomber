# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = None

# -

upstream = None

product = 'products/raw.csv'

import pandas as pd

df = pd.DataFrame({
    'A': [1,2,3,4,5],
    'B': [1,2,3,4,5],
})

df.to_csv(product)
