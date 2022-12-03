from mmap import MAP_PRIVATE
from os import access
import numpy as np

list1 = [2,5,8,6, 67.12]

ar1 = np.array(list1)
print(list1)
print(ar1)
list2 = [[1, 2], [3, 4], [5, 6]]

ar2 = np.array(list2)
print(ar2)

print(ar2 [2][0])
print(ar1.ndim)
print(ar2.shape)
print(ar2.size)
print(ar2.dtype)
print(ar2.itemsize)
#ar3 = np.zeros((17,17))
#print(ar3)
#ar4 = np.ones((17,17))
#print(ar4)
print(ar1 )
print(ar1 [0: 3] )

print(ar2)
print(ar2 [1: 2, 0:2 ])
ar3 = np.array([[1,2], [3,4] ])
ar4 = np.array([[5,6], [7,8]])
print("###")
print(ar3)
print("###")
print(ar4)
print("###")
print(ar3 + ar4)
print("#########")
print(ar3 - ar4)

print("#########")
print(ar3 * ar4)

print("#########")
print(ar3 / ar4)

print("#########")
print(ar3 // ar4)

print("#########")
print(ar4)
print(ar4.transpose())

print("#########")

ar5 = np.array([[44, 22, 77], [45, 23, 67], [235,2346, 1237]] )
print(ar5)
#ar5.sort(axis=  1)
print(ar5.max())
print(ar5.min())
print(ar5.sum())
print(ar5.mean())
print(ar5.std())
