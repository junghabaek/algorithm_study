whole_set = set(range(1, 10000))

num_set = set()
for i in range(10000):
    num = i
    for j in str(i):
        num += int(j)
    num_set.add(num)

whole_set = whole_set-num_set

sorted_set = sorted(list(whole_set))

for number in sorted_set:
    print(number)
