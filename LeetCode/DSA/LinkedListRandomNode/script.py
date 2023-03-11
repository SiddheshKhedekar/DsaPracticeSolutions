# Linked List Random Node -> Python3

'''
Explanation: We use reservoir sampling method to solve the problem. First initialize pointer res 
and index then loop while pointer. Inside check if random in limit 0 to i is 0 and set res to 
pointer val. Then set pointer to next and increment index.
'''

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
    def getRandom(self) -> int:
        res, pointer, indx = 0, self.head, 0
        while pointer:
            if random.randint(0, indx) == 0:
                res = pointer.val
            pointer = pointer.next
            indx += 1
        return res