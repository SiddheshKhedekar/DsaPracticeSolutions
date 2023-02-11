# Odd Even Linked List -> Python3

'''
Explanation: Start with odd and even as head and its next also set ehead as even. When in loop 
while even and its next set odd next to odd second next and same for even then set odd to odd next 
and same for even. Finally, outside loop set odd next to ehead.
'''

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        odd, even = head, head.next
        ehead = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = odd.next
        odd.next = ehead
        return head