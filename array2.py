import numpy as np

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr.shape)

newarr=arr.reshape(5,2)
print(newarr)


print("-----------------------------------")

for i in arr:
    print(i)


print("-----------------------------------")


for i in arr:
    for j in i:
        print(j)

print("-----------------------------------")

arr1=np.array([1,2,3])
arr2=np.array([3,4,5])

arr3=np.concatenate((arr1,arr2))
print(arr3)

print(arr3[1:3])

print("-----------------------------------")


arr4=np.stack((arr1,arr2))
print(arr4)


print("-----------------------------------")

arr5=np.hstack((arr1,arr2))
print(arr5)




print("-----------------------------------")

arr6=np.vstack((arr1,arr2))
print(arr6)

print("-----------------------------------")


arr7=np.array_split(arr1,1)
print(arr7)

print("-----------------------------------")

x=np.array([[1,2,3,4,5],[1,2,2,3,4]])
print(np.where(x == 3))