class Solution():
    def arraysep(self,a,b):
        c=[[],[]]
        for i in a :
            if i not in c[0]:
                c[0].append(i)
        for i in b:
            if i not in c[1] and i not in c[0]:
                c[1].append(i)
        return c


c=Solution()
b=[2,3,6,5,3]
a=[1,4,4,9,9]
b=[1,4,6,2,8]

print(c.arraysep(a,b))