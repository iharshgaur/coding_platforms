l=[4,3,2,7,8,2,3,1]
l.sort()
leng= len(l)-1
first=l[0]
last=l[leng]
n=[]
for i in range(first,last):
    if i not in l:
        n.append(i)
print(n)   
                            