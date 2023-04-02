# Diameter of Binary Tree -> Python3

'''
Explanation: Define global as ans 0 in main func and then define depth func inside. If not p return 
0 and set left, right to depth call to left, right child. Set ans to max ans and left+right return 
1+ max left, right. Call depth in main with root and return ans.
'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(p):
            if not p: return 0
            left, right = depth(p.left),depth(p.right)
            self.ans = max(self.ans, left+right)
            return 1+ max(left, right)
        depth(root)
        return self.ans