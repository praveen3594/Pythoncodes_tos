import pandas as pd


df=pd.read_csv('data.csv')


print(df)
print(df.to_string())




print("------------------------------------------------")
df2=pd.read_json('data.json')
print(df2)

print(df2.to_string())