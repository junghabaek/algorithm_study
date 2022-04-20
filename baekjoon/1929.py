m, n = map(int, input().split())

li = [2] 
lis=[]
for i in range(1, n+1):
    if i == 1 or i==2:
        continue

    check = 1
    for j in li:
        if i % j == 0:  # 소수가 아닌 경우
            check = 0
            break
        if j > int(i**0.5):
            break
    if check == 1:
        li.append(i)
        if i>=m:
            lis.append(i)

for j in lis:
    print(j)

#li에는 m까지의 소수들을 모아놓음
#m이 소수인 경우도 커버가 됨
#a b c d e ?


