T = int(input())


for i in range(T):
    S, str = input().split()
    ans = ''
    for letter in str:
        ans += letter*int(S)
    print(ans)
