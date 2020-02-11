num=10000
count=0
prime=0
if num<3:
    print(0)
else:
    for i in range(2,num):
        for j in range(2,num):
            if i!=j:
                if i%j==0:
                    count=count+1
        if count==0:
            prime=prime+1
        else:
            count=0
print(prime)
