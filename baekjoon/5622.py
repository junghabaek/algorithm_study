word = input()

cnt = 0
for letter in word:
    if ord(letter) < 68:  # 2
        cnt += 3
    elif ord(letter) < 71:  # 3
        cnt += 4
    elif ord(letter) < 74:  # 4
        cnt += 5
    elif ord(letter) < 77:  # 5
        cnt += 6
    elif ord(letter) < 80:  # 6
        cnt += 7
    elif ord(letter) < 84:  # 7
        cnt += 8
    elif ord(letter) < 87:  # 8
        cnt += 9
    elif ord(letter) < 91:  # 9
        cnt += 10
print(cnt)
