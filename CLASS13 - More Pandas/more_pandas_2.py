import pandas as pd
print(f'I am using {pd.__name__} \
Version: {pd.__version__}.\n\
It is installed at: {pd.__path__}')

prod = pd.read_csv('./Website Code/data/Production.Product.csv', sep="\t")
prod.head()
prod.set_index("ProductID", inplace=True)

print(prod)

prod["ProductLine"].value_counts().plot(kind="bar")


