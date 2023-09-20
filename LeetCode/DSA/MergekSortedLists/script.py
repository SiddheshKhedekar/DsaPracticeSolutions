# Merge k Sorted Lists -> Python3

'''
Explanation: Implement merge sort by first checking the base constraints and then setting middle by 
using length and left, right by recursive call to main function passing first and second parts of 
lists. Finally return the merge call of left and right. Inside merge function set temp and pointer 
and run loop while left and right. Check left less than right value and set pointer next and 
respective side next set pointer to its next and outside loop set pointer next to left or right 
before returning temp next.
'''

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left, right):
            temp = pointer = ListNode()
            while left and right:
                if left.val < right.val:
                    pointer.next = left
                    left = left.next
                else:
                    pointer.next = right
                    right = right.next
                pointer = pointer.next
            pointer.next = left or right
            return temp.next
        if not lists: return None
        if len(lists) == 1: return lists[0]
        mid = len(lists) // 2
        left, right = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return merge(left, right)