import pandas as pd
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
india = countries_counts["India"]
north_america = countries_counts[["USA", "Canada", "Mexico"]]
print(north_america)