import numpy as np

A=np.array([[1,2],[4,5]])
B=np.array([[5,6],[7,8]])

print(A+B)
print("----------------------")
print(A-B)

print("----------------------")
print(A*B)

print("----------------------")
print(A@B)

print("----------------------")
print(np.transpose(A))
      
print("----------------------")
print(np.sum(A))
print(np.mean(A))
print(np.max(A))
print(np.min(A))
print(np.median(A))

print("-----------------------------")

print(np.ones((2,3)))