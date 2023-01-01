# Binary Tree Pruning -> Python3

'''
Explanation: If root exist then assign root left and right to its respective side recursive call 
and then check if root and root left or right or val then return root.
'''

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root: root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        if root and (root.left or root.right or root.val): return root