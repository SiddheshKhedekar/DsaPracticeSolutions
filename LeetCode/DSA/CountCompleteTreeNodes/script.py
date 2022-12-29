# Count Complete Tree Nodes -> Python3

'''
Explanation: Use depth function to increment depth and call function for left and right side. If 
depth are equal then return depth + countNodes right side else depth + countNodes left side.
'''

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def getDepth(root):
            if not root: return 0
            return 1 + getDepth(root.left)
        if not root: return 0
        leftDepth, rightDepth = getDepth(root.left),  getDepth(root.right)
        if leftDepth == rightDepth: return pow(2, leftDepth) + self.countNodes(root.right)
        else: return pow(2, rightDepth) + self.countNodes(root.left)