# Remove Duplicates from Sorted List II -> Python3

'''
Explanation: Set empty listnode to dummy and pre. Iterate on head and if values of corresponding 
elements match then set head to its next else move to the next node.
'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next