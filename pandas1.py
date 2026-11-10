import pandas as pd

dataset={
    'cars':["BMW","Vovlo","Ford"],
    'passings':[2,7,2]
}

myvar=pd.DataFrame(dataset)

print(myvar)