import pandas as pd
import numpy as np

f500 = pd.read_csv('f500.csv', index_col=0)
f500.index.name = None
f500_head = f500.head(6)
f500_tail = f500.tail(8)
print(f500_head, '\n')
print(f500_tail)
f500.info()
industries = f500["industry"]
industries_type = type(industries)
print(industries_type)
print(industries.head(10))
countries = f500.loc[:, "country"]
revenues_years = f500.loc[:, ["revenues", "years_on_global_500_list"]]
ceo_to_sector = f500.loc[:, "ceo":"sector"]
print(countries)
print(revenues_years)
print(ceo_to_sector)
sectors = f500["sector"]
print(type(sectors))
sectors_value_counts = sectors.value_counts()
print(sectors_value_counts)
sectors_industries = f500[["sector", "industry"]]
print(type(sectors_industries))
countries = f500['country']
countries_counts = countries.value_counts()
india = countries_counts[["India"]]
north_america = countries_counts[["USA", "Canada", "Mexico"]]
print(india)
print(north_america)

assets = f500["assets"]
print(assets.describe())
print(countries.describe())

rank = f500["rank"]
rank_desc = rank.describe()
previous_rank = f500["previous_rank"]
prev_rank_desc = previous_rank.describe()
rank_change = f500["previous_rank"] - f500["rank"]
# Compute the number of 0 values in the previous_rank column to see how many companies were not on the list last year
zero_previous_rank = f500["previous_rank"].value_counts().loc[0]

f500.describe()
f500_numerics = f500.select_dtypes(include=np.number)
max_f500 = f500_numerics.max(axis=0)

