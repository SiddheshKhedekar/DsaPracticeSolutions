# Delete the Middle Node of a Linked List -> Python3

'''
Explanation: If head.next none then return none. Set slow and fast to head and head.next.next, 
while fast and fast.next set slow to slow.next and fast to fast.next.next, out of loop set 
slow.next to slow.next.next and return head.
'''

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: return None
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head