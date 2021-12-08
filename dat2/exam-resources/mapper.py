import sys
import pandas as pd

csv = [line.split(",") for line in sys.stdin.read().splitlines()]
df = pd.DataFrame(
    csv, columns=["salesperson", "capp_size", "tea_size", "capp_price", "tea_price"]
)
cap_df = df[["capp_size", "capp_price"]].set_index("capp_size")
tea_df = df[["tea_size", "tea_price"]].set_index("tea_size")
df = pd.concat([cap_df, tea_df]).fillna(0)
df[""] = df.capp_price.astype(float) + df.tea_price.astype(float)
df.drop(columns=["capp_price", "tea_price"], inplace=True)
print(df)
