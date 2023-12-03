# Merge Two Sorted Lists -> Python3

'''
Explanation: Initialize two dummy variables as listnode. Run a while loop for l1 and l2 not none. 
Inside while check if l2.next is greater than l1.next. In this condition set cursor.next as l1 and 
l1 as l1.next in else condition do same for l2. At end of condition set cur to cur next. Attach 
remaining nodes of l1 or l2 to cursor and return dummy.next.
'''

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) \
    -> Optional[ListNode]:
        temp = lis = ListNode()
        while list1 and list2:
            if list2.val > list1.val:
                lis.next = list1
                list1 = list1.next
            else:
                lis.next = list2
                list2 = list2.next
            lis = lis.next
        lis.next = list1 or list2
        return temp.next