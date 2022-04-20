

A, B, V = map(int, input().split())
if (V-B)//(A-B) == (V-B)/(A-B):
    print(int((V-B)/(A-B)))
else:
    print(int((V-B)/(A-B))+1)

# (A-B)*(x-1) +A >= V
# (A-B)*x-A+B+A>V
# (A-B)*x>V-B
# x>= (V-B)/(A-B)
# x>= 4/1 #x==4
# x>= 5/4 #x==2
# x>= (1000000000-99)/1
