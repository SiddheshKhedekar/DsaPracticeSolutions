# Linked List Cycle II -> Python3

'''
Explanation: Use slow fast and in loop when slow = fast break, in else of while return none and run 
a while loop again till slow != head set slow, head to head.next, slow.next and return head at end 
of loop.
'''

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        else: return None
        while head != slow: slow, head = slow.next, head.next
        return head