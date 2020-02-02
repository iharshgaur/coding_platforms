def swapcase(st):
    s=list(st)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=s[i].lower()
        elif s[i].islower():
            s[i]=s[i].upper()
    st="".join(s)
    return st

swapcase('HackerRank.com presents "Pythonist 2".')