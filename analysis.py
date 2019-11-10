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

# Answer some more basic questions about our data-set

# Select all rows from f500 that have a non-null value for the previous_rank columnpreviously_ranked
previously_ranked = f500.loc[f500["previous_rank"].notnull()]
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]
print(rank_change.shape)
# Assign the values in the rank_change to a new column in the f500 dataframe
f500["rank_change"] = rank_change
# Now select all companies with revenues over 100 billion and negative profits from the f500 dataframe.
large_revenue = f500["revenues"] > 100000
negative_profits = f500["profits"] < 0
combined = large_revenue & negative_profits
big_rev_neg_profit = f500.loc[combined]
# Select all rows for companies headquartered in either Brazil or Venezuela
brazil_venezuela_bool = (f500["country"] == "Brazil") | (f500["country"] == "Venezuela")
brazil_venezuela = f500.loc[brazil_venezuela_bool]
# Select the first five companies in the Technology sector that are not headquartered in the USA
tech_outside_usa_bool = (f500["sector"] == "Technology") & (~(f500["country"] == "USA"))
tech_outside_usa = (f500.loc[tech_outside_usa_bool]).head()

# Let's answer more complex questions about our data set
# Find the company headquartered in Japan with the largest number of employees.
japanese_companies = f500.loc[f500["country"] == "Japan",:]
# sort the companies based on employees
japanese_companies = japanese_companies.sort_values("employees", ascending=False)
print("Largest Japanese employer in list:", japanese_companies.head(1)["employees"])
# Based on the data, the Japanese company that employs the most people is Toyota Motor.
print(japanese_companies.head(1))

# Now let's produce a dictionary of the top employer in each country
top_employer_by_country = {}
# create an array of unique values from the country column
countries = f500["country"].unique()
for c in countries:
    # Get rows that have a country name equal to the current iteration
    df_c = f500.loc[f500["country"] == c, :]
    # sort those rows by the employees column in descending order
    df_c = df_c.sort_values("employees", ascending=False)
    # Get and store the company name into the dictionary keyed by country name
    top_employer = (df_c.head(1).index[0])
    top_employer_by_country[c] = top_employer
print(top_employer_by_country)

# Aggregate the data by the sector column, and create a dictionary top_roa_by_sector
f500["roa"] = f500["profits"] / f500["assets"]
top_roa_by_sector = {}
unique_sectors = f500["sector"].unique()
for sector in unique_sectors:
    # Find company name with the highest ROA value from the current sector
    df_sector = f500.loc[f500["sector"] == sector]
    # sort values in descending order so we can easily get the highest ROA
    df_sector = df_sector.sort_values("roa", ascending=False)
    # update the dictionary keys with the sector name
    # dictionary value is the company name with the highest ROA value from that sector
    top_roa_company = (df_sector.head(1)).index[0]
    top_roa_by_sector[sector] = top_roa_company
print("\n", top_roa_by_sector)
