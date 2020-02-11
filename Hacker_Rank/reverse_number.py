def reversexber():
    x=120
    if x<0:
        print("False")
    temp=x
    rev=0
    while x>0:
        dig=x%10
        rev=rev*10+dig
        x=x//10
    if temp==rev :
        print("True")
    else:
        print("False")
reversexber()