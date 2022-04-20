n= int(input())

num=n
li=[]
for i in range(2,n+1):
    while num%i==0:
        num=num//i
        li.append(i)
    if num==1:
        for _ in li:
            print(_)
        break

