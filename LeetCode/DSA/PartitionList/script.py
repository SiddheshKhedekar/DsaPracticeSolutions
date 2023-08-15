# Partition List -> Python3

'''
Explanation: Set head1 as list1 as new listnode and same for head2 and list2. Loop while head and 
check if head val is less than x to set list1 next as head and list1 as its next then same for 
list2 in else. After loop end set list2 next as none and list1 next as head2 next before returning 
head1 next.
'''

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head1 = list1 = ListNode(0)
        head2 = list2 = ListNode(0)
        while head:
            if head.val < x:
                list1.next = head
                list1 = list1.next
            else:
                list2.next = head
                list2 = list2.next
            head = head.next
        list2.next = None
        list1.next = head2.next
        return head1.next