# -*- coding: utf-8 -*-
import sys
import math
def find_mc(ac,bc):
    theta= str(int(round(math.degrees(math.atan2(ac, bc)))))+'°'
    sys.stdout.write(theta)

ac=sys.stdin.readline()
ac=int(ac)
bc=sys.stdin.readline()
bc=int(bc)
find_mc(ac,bc)


