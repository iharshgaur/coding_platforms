def solve(s):
    name= s.split(' ')
    for i in range(len(name)):
        name[i]=name[i].capitalize()
    s= " ".join(name) 
    return s

print(solve('1 2 2 3 4 5 6 7 8  9'))