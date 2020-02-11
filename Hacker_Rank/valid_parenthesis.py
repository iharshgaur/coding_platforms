def check(s):
    open_tup = tuple('({[')
    close_tup = tuple(')}]')
    map = dict(zip(open_tup, close_tup))
    l = []
    p=list(s)
    flag=0
    for i in p:
        if i=="{":
            flag=flag+1
        elif i=="[":
            flag=flag+1
        elif i=="(":
            flag=flag+1
        elif i==")":
            flag= flag-1
        elif i=="]":
            flag= flag-1
        elif i=="}":
            flag= flag-1
    if flag==0:
        for i in s:
            if i in open_tup:
                l.append(map[i])
            elif i in close_tup:
                if not l or i != l.pop():
                    return False
        return True
    else:
        return False
string = "{([)]}"
print(check(string)) 
