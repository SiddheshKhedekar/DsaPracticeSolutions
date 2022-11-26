# Intersection of Two Linked Lists -> Python3

'''
Explanation: If first list(a) is none or second list(b) is none return none. Set temp variables pa 
and pb to a and b. While pa is not pb run loop set temp variables to the othere list if temp is 
none else set temp variables to their next and return pa after loop end.
'''

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None: return None
        pa, pb = headA, headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa