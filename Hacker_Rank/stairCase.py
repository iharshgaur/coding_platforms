
def stair():
    stairs=7
    if stairs==1:
        return 1
    elif stairs==2:
        return 2
    elif stairs==3:
        return 3
    else:
        i=3
        j=2
        temp=0
        k=1
        while k<=stairs-3:
            temp=i
            i=i+j
            j=temp
            k=k+1
        return i
stair()