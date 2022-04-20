word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

cnt = 0
for letter in word:
    for abc in dial:
        if letter in abc:
            cnt += dial.index(abc)+3
print(cnt)
