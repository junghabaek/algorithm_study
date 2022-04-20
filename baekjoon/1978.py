N = int(input())
li = list(map(int, input().split()))
cnt = N
for i in range(N):
    if li[i] == 1:
        cnt -= 1
        continue
    for j in range(2, li[i]):
        if li[i]%j == 0:
            cnt -= 1
            break
print(cnt)
