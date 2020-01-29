def reverse(num):
    rev=0
    while(num > 0):
        rem = num %10
        rev = (rev*10) + rem
        num = num //10 
    return rev

n= int(input())
prev=0
for i in range(1,int(input())+1):
    print((prev*10+i)*(10**i-1)+reverse(prev))
    prev=prev*10+i