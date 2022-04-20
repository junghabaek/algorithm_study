N = int(input())
cnt = 0

for i in range(N):
    word = input()
    new_word = word
    cnt+=1
    for letter in word:
        new_word = new_word.lstrip(letter)
        if letter in new_word:
            cnt-=1
            break
    
print(cnt)
