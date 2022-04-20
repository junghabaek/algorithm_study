import sys
C = int(sys.stdin.readline())

li = []
for i in range(C):
    N, *student_grade = map(int, sys.stdin.readline().split())
    total = 0
    total = sum(student_grade)
    avg = total/N
    cnt = 0
    for i in student_grade:
        if i > avg:
            cnt += 1
    li.append('{:.3f}'.format(round(100*cnt/N, 3)))

for i in li:
    print(i, '%', sep='')
