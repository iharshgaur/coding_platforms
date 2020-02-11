if __name__ == '__main__':
    s = input()
    al=0
    alnum=0
    dig=0
    up=0
    low=0
    for i in s:
        if i.isalnum():
            alnum=1
        if i.isalpha():
            al=1
        if i.isdigit():
            dig=1
        if i.islower():
            low=1
        if i.isupper():
            up=1
    
    if alnum==1: print(True)
    else: print(False)
    if al==1: print(True)
    else: print(False)
    if dig==1: print(True)
    else: print(False)
    if low==1: print(True)
    else: print(False)
    if up==1: print(True)
    else: print(False)