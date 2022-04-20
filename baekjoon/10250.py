# import sys
# H, N = map(int, sys.stdin.readline().split())

# print (N%H)

import sys
T = int(sys.stdin.readline())


for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    if N%H!=0:
        print(str(N % H)+str(N//H+1).zfill(2))
    else:
        print(str(H)+str(N//H).zfill(2))
