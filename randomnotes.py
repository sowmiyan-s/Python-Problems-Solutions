ransomNote='aa'
magazine='aab'
def canConstruct(ransomNote, magazine):
    d={}
    for i in magazine:
        if i not in d:
            d[i]= magazine.count(i)
    for i in ransomNote:
        if i not in d:
            return False
        if d[i] < ransomNote.count(i):
            return False
    return True 
print(canConstruct(ransomNote, magazine))