class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1=ListNode(l1)
        s2=ListNode(l2)
        print(s1)
        """ a=s1.split('->')
        b=s2.split('->')
        a=a+b
        a.sort()
        i=0
        for i in range(len(a)):
            if i< len(a)-1:
                print(a[i]+'->',end='')
            else:
                print(a[i]) """
   
        