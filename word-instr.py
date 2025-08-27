word1='abbc'
word2='cbjdba'
a=list(word1)
b=list(word2)

for i in a:
    b.pop(i)
print(a)