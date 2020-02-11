maxim=0
total=0
b=[]
i= int(input())

for p in range(0,i):
    b.append(int(input()))
b.sort()

for a in b:
    if a>0:
        total = a*i
        if total>maxim:
            maxim=total
        i=i-1
print(maxim)
