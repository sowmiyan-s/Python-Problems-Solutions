word = input()
current , total = 0 , 1
for i in range(0,len(word)):
    if word[i] == word[i-1]:
        current += 1
        total = max(current,total)

    else:
        current = 1
print(total)

