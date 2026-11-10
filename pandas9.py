import pandas as pd


df=pd.read_csv('data.csv')
df.loc[7,"Duration"]=56


for x in df.index:
    if df.loc[x,'Duration']>120:
        df.drop(x)


print("----------------------")
print(df.duplicated())

df.drop_duplicates()

print(df.corr())

df.plot()