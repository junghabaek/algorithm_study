m, n = int(input()), int(input())

li=list(range(m,n+1))
for i in range(m, n+1):
    if i==1: 
        li.remove(i)
    for j in range(2,i):
        if i%j==0:
            li.remove(i)
            break
if len(li)==0:
    print(-1)
else:
    print(sum(li))
    print(min(li))
