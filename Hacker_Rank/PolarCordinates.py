# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import cmath
import re

inp=sys.stdin.readline()
inp=inp.strip("j")
rx = re.compile(r'-?\d+?')
factors = rx.findall(inp)
i=int(factors[0])
j=int(factors[1])
a=abs(complex(i,j))
c=cmath.phase(complex(i,j))
sys.stdout.write(str(a))
sys.stdout.write('\n')
sys.stdout.write(str(c))
