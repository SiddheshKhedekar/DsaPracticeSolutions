# Swap Nodes in Pairs -> Python3

'''
Explanation: Check if not head and return it then set pre, cur, res as none, head and its next. 
Then run loop while cur and its next then set adj to next cur. Check if pre to set next of pre as 
adj then set cur next as adj next and adj next as cur also pre as cur and cur as its next. Finally 
out of loop return res or head.
'''

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        pre, current, res = None, head, head.next
        while current and current.next:
            adjacent = current.next
            if pre: pre.next = adjacent
            current.next, adjacent.next = adjacent.next, current
            pre, current = current, current.next
        return res or head