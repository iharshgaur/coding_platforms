i = input ()
i=i.strip()
s= list(i)
print(s)
if (len(s)/2)==0:
    s[int(len(s)/2)]="*"
    print(' '.join(s))