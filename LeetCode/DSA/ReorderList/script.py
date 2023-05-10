# Reorder List -> Python3

'''
Explanation: Find mid using slo, fas technique. Reverse the second half using pre, cur, nex and 
merge the two lists using head1 and head2.
'''

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return []
        slo, fas = head, head
        while fas.next and fas.next.next:
            slo, fas = slo.next, fas.next.next
        pre, cur = None, slo.next
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        slo.next = None
        h1, h2 = head, pre
        while h2:
            nex = h1.next
            h1.next = h2
            h1 = h2
            h2 = nex