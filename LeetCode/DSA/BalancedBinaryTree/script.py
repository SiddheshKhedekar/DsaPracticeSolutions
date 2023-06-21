# Balanced Binary Tree -> Python3

'''
Explanation: Return check(root) != -1. Inside subfunction if root none return 0, assign left, right 
to check root left and right, if left or right is -1 or abs left-right > 1 return -1 and finally 
return 1 + max left, right.
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root is None: return 0
            left, right = check(root.left), check(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1: return -1
            return 1 + max(left,right)
        return check(root) != -1