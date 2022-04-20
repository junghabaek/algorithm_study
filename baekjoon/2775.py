T = int(input())


def answer(k, n):
    if n == 1:
        return 1
    if k == 0:
        return n
    else:
        ret = 0
        for i in range(1, n+1):
            ret += answer(k-1, i)
        return ret


for i in range(T):
    k=int(input())
    n=int(input())
    ans = answer(k, n)
    print(ans)

# k층 n호

# 1+1+1+2 = 1+1+1+2

# 1 1+1+1+2 1+(1+1+2)+(1+1+2+1+2+3) -> k층 n호는 k-1층 1호 + ... + k-1층 n-1호
# 1 1+1+2 1+1+2+1+2+3
# 1 1+2 1+2+3 ... 1+...+n -> k층 m까지의 합을 일반화 해서 답을 구해보자
# 1 2 3... n

# k층 n호는 = k층 n-1호 + k-1층 n-1호 + k-2층 n호
# =k층 n-1호 + k-1층 n-1호 + k-2층 n-1호 + k-3층 n호...

# num = 0
# for i in range(k+1):
#     for j in range(1, n+1):
#         num += j
#         summ = num




# 1 1+2 1+2+3
# 1 2 3

# answer(1, 3)= answer(0, 1) + answer(0, 2) + answer(0,3)


# T = int(input())
# k, n = map(int, input().split())


# k층 n호

# 1+1+1+2 = 1+1+1+2

# 1 1+1+1+2 1+(1+1+2)+(1+1+2+1+2+3)+-> k층 n호는 k-1층 1호 + ... + k-1층 n-1호
# 1 1+1+2 1+1+2+1+2+3     k=0 1 2 3 k=1 1 3 6 10 15 21 k=2 1 4 10 20 35... 3 6 10 15
# 1 1+2 1+2+3 1+2+3+4 1+2+3+4+5... 1+...+n -> k층 m까지의 합을 일반화 해서 답을 구해보자
# 1 2 3... n

# k층 n호는 = k층 n-1호 + k-1층 n-1호 + k-2층 n호
# =k층 n-1호 + k-1층 n-1호 + k-2층 n-1호 + k-3층 n호...

# num = 0
# for i in range(k+1):
#     for j in range(1, n+1):
#         num += j
#         summ = num


# def answer(k, n):
#     if k == 0:
#         return ((n*(n+1)/2))
#     else:
#         ret = 0
#         for i in range(1, n):
#             ret += answer(k-1, i)
#         return ret


# t = int(input())

# for _ in range(t):
#     floor = int(input())  # 층
#     num = int(input())  # 호
#     f0 = [x for x in range(1, num+1)]  # 0층 리스트
#     for k in range(floor):  # 층 수 만큼 반복
#         for i in range(1, num):  # 1 ~ n-1까지 (인덱스로 사용)
#             f0[i] += f0[i-1]  # 층별 각 호실의 사람 수를 변경
#     print(f0[-1])  # 가장 마지막 수 출력

T = int(input())

for _ in range(T):
    k=int(input())
    n=int(input())
    #k는 층수
    #n은 몇 호
    li = [x for x in range(1, n+1)]
    for i in range(1, k+1):
        for j in range(1, n):  # index로 사용
            li[j] = li[j]+li[j-1]
    print(li[-1])
