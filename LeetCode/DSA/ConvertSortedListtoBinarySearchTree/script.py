# Convert Sorted List to Binary Search Tree -> Python3

'''
Explanation: If not head then return and if not its next then return treenode with head val. Set 
slo and fas and in while loop get the middle then set temp to next of middle and then set slo next 
to None. Set root to treenode temp val and left and right to recursive call to head and temp next.
'''

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return
        if not head.next: return TreeNode(head.val)
        slo, fas = head, head.next.next
        while fas and fas.next:
            fas = fas.next.next
            slo = slo.next
        temp = slo.next
        slo.next = None
        root = TreeNode(temp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)
        return root