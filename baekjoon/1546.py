N = int(input())

li = []
for i in range(N):
    li.append(int(input()))
M = max(li)

ans = 0
for i in range(N):
    ans += (li[i]/M*100)
print(ans/N)
