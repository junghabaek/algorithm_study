word = input()
word = word.upper()

letters = {}

for letter in word:
    letters[letter] = letters.setdefault(letter, 0) + 1

max_val = max(letters.values())
cnt = 0
for value in letters.values():
    if value == max_val:
        cnt += 1

if cnt > 1:
    print('?')
else:
    print(max(letters.keys(), key=lambda k: letters[k]))
