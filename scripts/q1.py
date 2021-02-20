import numpy as np

A = [5,7,8,10,15]
B = [2,5,7,9,12]

arrA = np.array(A)
arrB = np.array(B)

arrC = np.concatenate([arrA, arrB])

sortedC = np.sort(arrC)

sortedC = np.unique(sortedC)

C = sortedC.tolist()

print(C)