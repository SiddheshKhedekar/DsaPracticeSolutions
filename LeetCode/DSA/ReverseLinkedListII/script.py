# Reverse Linked List II -> Python3

'''
Explanation: Check for base condition then set prev, temp as listnode and temp next as head. Then 
loop on range left - 1 to set prev to its next and after loop end set tail as prev next. Then loop 
on range right - left to reverse list using tmp and return temp next at end.
'''

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right: return head
        prev = temp = ListNode(None)
        temp.next = head
        for _ in range(left - 1): prev = prev.next
        tail = prev.next
        for _ in range(right - left):
            tmp = prev.next
            prev.next = tail.next
            tail.next = tail.next.next
            prev.next.next = tmp
        return temp.next