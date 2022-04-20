N = int(input())
line = 1  # 숫자가 있는 전줄 까지의 갯수

while N > line:
    N -= line
    line += 1

if line % 2:
    a = line-N+1
    b = N
else:
    a = N
    b = line-N+1
print(f'{a}/{b}')
