import sys
import pandas as pd

csv = [line.split(",")[0].split() for line in sys.stdin.read().splitlines()][1:]
df = pd.DataFrame(csv, columns=["type_size", "price"]).set_index("type_size")
df.price = pd.to_numeric(df.price)


df = df.groupby(level=0).sum()
df.rename(columns={"price": ""}, inplace=True)
df.index.name = None
print(df)
