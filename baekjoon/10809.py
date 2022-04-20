word = input()

alphabet = [-1 for x in range(26)]

for letter in word:  # a 자리에 a의 index를 쓰기
    alphabet[ord(letter)-97] = word.index(letter)

for i in alphabet:
    print(i, end=' ')
