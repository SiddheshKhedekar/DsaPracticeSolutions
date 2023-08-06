# Sort List -> Python3

'''
Explanation: Inside main function use dolw fast and set start as middle then call sortlist on head, 
start to set left, right then return the merge of left, right. Inside merge set dummy, prev and 
loop while left and right to merge the list finally returning dummy next.
'''

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(left, right):
            if not left or not right: return left or right
            dummy = prev = ListNode(0)
            while left and right:
                if left.val < right.val:
                    prev.next = left
                    left = left.next
                else:
                    prev.next = right
                    right = right.next
                prev = prev.next
            prev.next = left or right
            return dummy.next
        if not head or not head.next: return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        start = slow.next
        slow.next = None
        left, right =  self.sortList(head), self.sortList(start)
        return merge(left, right)