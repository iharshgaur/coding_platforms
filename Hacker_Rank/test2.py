class Solution:
    # @param A : integer
    # @return a list of list of integers
    def squareSum(self, A):
        ans = []
        A=int(A)
        b = int(A**0.5)
        a=1
        while b>=0 :
            while a <=b:
                if a**2 + b**2 == A:
                    newlist=[a,b]
                    ans.append(newlist)
                a= a+1
            b=b-1
        print(ans)
    squareSum(7873,7873)