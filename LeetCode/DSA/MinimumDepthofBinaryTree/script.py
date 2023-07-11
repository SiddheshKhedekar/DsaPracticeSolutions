# Minimum Depth of Binary Tree -> Python3

'''
Explanation: We add the smaller one of the children depths unless if that's zero, then add the 
larger one.
'''

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        x, X = sorted(map(self.minDepth, (root.left, root.right)))
        return 1 + (x or X)