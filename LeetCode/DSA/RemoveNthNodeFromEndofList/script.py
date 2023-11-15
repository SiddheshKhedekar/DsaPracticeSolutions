# Remove Nth Node From End of List -> Python3

'''
Explanation: Use fast slow pointers assign both to head first. For loop in range n set fast to 
fast.next. Out of loop check if not fast and return head.next. Run while loop outside condition 
till fast.next and set fast and slow to their respective next. Outside set slow.next to 
slow.next.next and finally return head.
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head