import sys
from itertools import permutations

def permu(stri,num):
    for i in list(permutations(stri,num)):
        j= list(i)
        for l,k in enumerate(j):
            j[l]=k.upper()
        j.sort()
        sys.stdout.write("".join(j)+"\n")


line1 = sys.stdin.readline()
n=line1.split(" ")
permu(n[0],int(n[1]))