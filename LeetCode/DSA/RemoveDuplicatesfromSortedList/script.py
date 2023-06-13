# Remove Duplicates from Sorted List -> Python3

'''
Explanation: Initialize current to head. While current and its next exist run loop. Check if cur 
val equals to the cur next val then set cur next to cur next next else set cur to the next. Return 
head after loop.
'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val: cur.next = cur.next.next
            else: cur = cur.next
        return head