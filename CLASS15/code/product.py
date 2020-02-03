# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import pandas as pd
import numpy as np # used for linear algebra and random sampling
# used for plotting charts within the notebook (instead of a separate window)
get_ipython().run_line_magic('matplotlib', 'inline')
prod = pd.read_csv('../data/Production.Product.csv', sep='\t')
prod.head(3)
prod.shape
prod.describe()


# %%
prod.columns


# %%
prod.info


# %%
prod.notnull()
prod.notnull().sum()
x = 2

prod["Color"]
prod["Color"].value_counts(dropna=True)

prod["Color"].dropna() # never just drop NA on the column
# %%
