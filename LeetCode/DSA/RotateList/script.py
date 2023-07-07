# Rotate List -> Python3

'''
Explanation: Firstly get the length and the last element of the list then handle k if greater than 
l by mod. Set last node to head making list circular then loop k - l times to set node to its next. 
Set res then remove circular link.
'''

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        lEle, l = head, 1
        while(lEle.next):
            lEle = lEle.next
            l += 1
        k = k % l
        lEle.next = head
        node = head
        for _ in range(l - k - 1): node = node.next
        res = node.next
        node.next = None
        return res