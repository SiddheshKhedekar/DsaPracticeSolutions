# Swapping Nodes in a Linked List -> Python3

'''
Explanation: Find the k-th node from the front then find the k-th last element using two poiners 
method. Swap their values and return the head of the Linked List.
'''

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = end = head
        for _ in range(1, k): start = start.next
        dummy = start
        while dummy.next: end, dummy = end.next, dummy.next
        start.val, end.val = end.val, start.val
        return head