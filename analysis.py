import pandas as pd
f500 = pd.read_csv('f500.csv', index_col=0)
f500.index.name = None
f500_head = f500.head(6)
f500_tail = f500.tail(8)
print(f500_head, '\n')
print(f500_tail)
