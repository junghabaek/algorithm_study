import sys
a = int(sys.stdin.readline())
num = a
cnt = 0

while 1:
    if a < 10:
        a = a*11
        cnt += 1
        if a == num:
            break
    else:
        b = a//10+a % 10
        a = a % 10*10+b % 10
        cnt += 1
        if a == num:
            break
print(cnt)
