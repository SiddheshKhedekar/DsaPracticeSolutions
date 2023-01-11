# Reverse Linked List -> Python3

'''
Explanation: Initialize a prev to none then in a while loop for head, set temp to head, head to its 
next, next of temp to prev and prev to temp. Outside loop return prev.
'''

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev