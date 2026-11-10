import pandas as pd

a=[1,6,9]

myvar=pd.Series(a,index=["x","y","z"])
print(myvar)
print(myvar["y"])



calories={"day1":100,"day2":120,"day3":390}
myvar2=pd.Series(calories)
myvar3=pd.Series(calories,index=["day1","day2"])
print(myvar2)
print(myvar3)



print("--------------------------------------------")
cal={"calories":[420,380,190],"duration":[45,80,56]}
myvar4=pd.DataFrame(cal)
print(myvar4)

print(myvar4.loc[0])

print(myvar4.loc[1])

print("--------------------------------------------")


myvar5=pd.DataFrame(cal,index=["a","b","c"])
print(myvar5)