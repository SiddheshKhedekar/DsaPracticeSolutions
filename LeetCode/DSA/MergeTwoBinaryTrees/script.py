# Merge Two Binary Trees -> Python3

'''
Explanation: If root1 none then return root2 same for root2 viceversa. Increment root1 val with 
root2 val. Set root1 left to recursive call root1 left and root2 left do the same for right and 
return root1.
'''

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None: return root2
        if root2 is None: return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1