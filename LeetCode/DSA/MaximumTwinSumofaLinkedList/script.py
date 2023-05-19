# Maximum Twin Sum of a Linked List -> Python3

'''
Explanation: Get middle of linked list using slo/fas then reverse second part of linked list using 
cur/prev. Finally, in loop get max sum of pairs.
'''

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slo, fas, mxVal = head, head, 0
        while fas and fas.next: fas, slo = fas.next.next, slo.next
        curr, pre = slo, None
        while curr: curr.next, pre, curr = pre, curr, curr.next
        while pre:
            mxVal = max(mxVal, head.val + pre.val)
            pre, head = pre.next, head.next
        return mxValxcc