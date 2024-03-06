# Linked List Cycle -> Python3

'''
Explanation: Set slow and fast pointer to head then loop while fast and its next are valid to 
update slow to its next and fast to its next of next. Check if slow is same as fast and return true 
otherwise outside loop return false.
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False