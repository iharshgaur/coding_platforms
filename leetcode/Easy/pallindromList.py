l="1->2->2"
n=list(l.split("->"))
leng=len(n)
j=leng-1
flag=0
for i in range(0,leng//2):
    if n[i]==n[j]:
        pass
    else:
        flag=1
    j=j-1 
if flag==1:
    print("false")
else:
    print("true")
