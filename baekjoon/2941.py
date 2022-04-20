c_alphabet = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']


word = input()

cnt = 0

for letter in c_alphabet:
    if letter in word:
        word = word.replace(letter, 'A')

print(word)
print(len(word))
