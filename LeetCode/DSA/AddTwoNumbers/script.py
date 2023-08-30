# Add Two Numbers -> Python3

'''
Explanation: Initialize new cur = dum =new listnode0 run loop while l1 or l2 or cary set v1 v2 to 0 
and check if l1 l2 individually and do the same set v to l val and l to l next set cart and val to 
divmod cary and v values , 10 dum next is listnode val and dum becomes dum next finally out of loop 
return cur next.
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dumhead = ListNode(0)
        cary = 0
        while l1 or l2 or cary:
            v1 = v2 = 0
            if l1: v1, l1 = l1.val, l1.next
            if l2: v2, l2 = l2.val, l2.next
            cary, val = divmod(v1+v2+cary,10)
            dumhead.next = ListNode(val)
            dumhead = dumhead.next
        return cur.next