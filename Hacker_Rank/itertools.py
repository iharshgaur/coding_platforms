import sys
from itertools import product

line1=sys.stdin.readline()
line1=list(map(int,line1.split()))
line2=sys.stdin.readline()
line2=list(map(int,line2.split()))


for i in list(product(line1,line2)):
    sys.stdout.write(str(i))
    sys.stdout.write(' ')