# Invert Binary Tree -> Python3

'''
Explanation: If root does not exist return root. Below this condition assign left to root left and 
right to root right. Set root left to recursive call of same function passing right value and same 
for root right vice versa.
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return root
        left, right = root.left, root.right
        root.left, root.right = self.invertTree(right), self.invertTree(left)
        return root