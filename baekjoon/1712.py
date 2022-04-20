import math
A, B, C = map(int, input().split())

if C-B<=0:
    print('-1')
else:

    if A/(C-B) == math.ceil(A/(C-B)):
        print(int(1+A/(C-B)))
    else:
        print(math.ceil(A/(C-B)))
