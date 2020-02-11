import sys
from itertools import permutations

def permute(string,nu):
    lst=[]
    for i in permutations(string):
        b = '"{}"'.format("".join(i))
        lst.append(b)
    print('#{}'.format(nu))
    values = ','.join(map(str, lst))
    print(values)

def sorting(string):
    st=[]
    for w in string:
        st.append(w)

    sort= sorted(st)
    print('\u201c{}\u201d'.format("".join(sort)))
    
line1 = sys.stdin.readline()
n=line1.split(" ")
line2 = sys.stdin.readline()
line=line2.split(" ")
permute(line[0],n[0])
sorting(line[0])