N = int(input())

low_end = 2
cnt = 1
#2- 8- 20- 38-
while True: 
    if N >= low_end: #20 ans=4
        low_end = low_end+6*cnt #8 8+6*2
        cnt += 1 #2 3
    else:
        break
print(cnt)
