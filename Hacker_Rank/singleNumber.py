li=[2,2,1]
li.sort()
counts=0
for i in li:
    counts=li.count(i)
    if counts==1:
        print(i)
    
    