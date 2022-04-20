import sys

n = int(sys.stdin.readline())

hansoo = []
for num in range(1, n+1):
    if 100<num<1000:
        temp_list = []
        for i in str(num):  # 1 # 12 #123
            temp_list.append(int(i))
        if temp_list[0]-temp_list[1] == temp_list[1]-temp_list[2]:
            hansoo.append(num)
    elif 0<num<100:
        hansoo.append(num)


print(len(hansoo))
