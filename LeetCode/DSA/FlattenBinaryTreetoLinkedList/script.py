# Flatten Binary Tree to Linked List -> Python3

'''
Explanation: Define pre as none in init function and in main check if not root to return none then 
call flatten on right and left. Set root right to pre, left to none and pre to root.
'''

class Solution:
    def __init__(self): self.pre = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root: return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.pre
        root.left = None
        self.pre = root