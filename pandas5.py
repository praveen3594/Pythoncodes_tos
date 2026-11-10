import pandas as pd

df=pd.read_csv('data.csv')


print(df.head(10))
print(df.tail(10))
print(df.info())


new_df=df.dropna()
print(new_df.tail())

df.fillna(100,inplace=True)
x=df["Calories"].mean()
x=df["Calories"].median()
x=df["Calories"].mode()[0]
df.fillna({"Calories":x}, inplace=True)


