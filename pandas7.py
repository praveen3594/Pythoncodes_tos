import pandas as pd


df=pd.read_csv('data.csv')


new_df=df.dropna()


print(df)
print(new_df)

df.dropna(inplace=True)

df.fillna(100)


x=df["Calories"].mean()

df.fillna({"Calories":x},inplace=True)