N = int(input())

li = []
for i in range (N//5+1):
    if (N-(i*5))%3==0:
        li.append(i+(N-(i*5))//3)
if len(li)==0:
    print(-1)
else:
    print(min(li))