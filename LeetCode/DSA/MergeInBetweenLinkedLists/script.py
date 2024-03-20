# Merge In Between Linked Lists -> Python3

'''
Explanation: Set beg to none, end to list1 then loop for x in range b and check if x is a - 1 to 
set beg to end then set end to its next in loop. Then outside loop set beg next to list2 and loop 
while list2.next to set list to list2 next. Outside thiis loop set list2 next to end next and end 
next to none before returning list1. Locate node right before a and b upon end of the first loop. 
Connect the node right before a to the head of list2, hence cut off a from list1. Traverse till the 
end of list2 then connect end of list2 to the node right after b and cut off b from list1.
'''

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        beg, end = None, list1
        for x in range(b):
            if x == a - 1: beg = end
            end = end.next
        beg.next = list2
        while list2.next: list2 = list2.next
        list2.next = end.next
        end.next = None
        return list1 