# cook your dish here
def getInvCount(i, n): 
    inv_count = 0
    for y in range(n): 
        for z in range(y+1, n): 
            if i[y] > i[z]:
                inv_count += 1
    print(inv_count)
    return inv_count 
k=[]
n=[]
s=[]
T=input()
T =int(T)
for i in range(0,T):
    N,K=input().split()
    N=int(N)
    n.append(N)
    K=int(K)
    k.append(K)
    A=input()
    arr=list(A.split())
    arr=arr*K
    s.append(arr)
for i in s:
    if 1<=T<=1000 and 1<=N<=100 and 1<=K<=10**6:
        n = len(i)
        getInvCount(i, n)