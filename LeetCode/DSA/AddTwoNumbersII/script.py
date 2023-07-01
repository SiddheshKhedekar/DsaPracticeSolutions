# Add Two Numbers II -> Python3

'''
Explanation: As we can not reverse our original lists we put them into a stack then iterate over 
the first and the second lists and create two stacks. Iterate over stacks, pop last elements from 
stack if possible, if not, use 0 for empty stack. Add these two numbers and evaluate next digit and 
carry. Create new node with digit and attach it before current dummy, update it. Finally we return 
dummy in the end.
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1, stk2, cary, dummy = [], [], 0, None
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        while stk1 or stk2 or cary:
            dgt1, dgt2 = 0, 0
            dgt1 = stk1.pop() if stk1 else 0
            dgt2 = stk2.pop() if stk2 else 0
            cary, dgt = divmod(dgt1 + dgt2 + cary, 10)
            dummy_new = ListNode(dgt)
            dummy_new.next = dummy
            dummy = dummy_new
        return dummy