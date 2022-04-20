import numpy as np
n = input()
array = np.array(map(int, input().split()))
print(array.min, array.max)
