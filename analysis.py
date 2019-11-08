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
# alternatively, we could use the line of code below:
max_f500_alt = f500.max(numeric_only=True)

# Update a value in the dataframe
f500.loc["Dow Chemical", "ceo"] = "Jim Fitterling"
# temporaly display 999 rows
# with pd.option_context('display.max_rows', 999):
#     print(f500["ceo"])
motor_bool = f500["industry"] == "Motor Vehicles and Parts"
motor_countries = f500.loc[motor_bool,"country"]
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
# Boolean indexing to update values in the previous_rank column of the f500 dataframe
previous_rank_bool = f500["previous_rank"] == 0
f500.loc[previous_rank_bool,"previous_rank"] = np.nan
prev_rank_after = f500["previous_rank"].value_counts(dropna=False).head()
bool_usa = f500["country"] == "USA"
industry_usa = f500.loc[bool_usa,"industry"].value_counts().head(2)

bool_china = f500["country"] == "China"
sector_china = f500.loc[bool_china,"sector"].value_counts().head(3)
