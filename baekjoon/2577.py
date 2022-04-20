A = int(input())
B = int(input())
C = int(input())
result = A*B*C

dic = {}
for i in str(result):
    dic[i] = dic.setdefault(i, 0)+1

for i in '0123456789':
    try:
        print(dic[i])
    except:
        print('0')
