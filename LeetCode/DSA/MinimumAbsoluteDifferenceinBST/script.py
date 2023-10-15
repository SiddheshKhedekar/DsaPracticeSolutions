# Minimum Absolute Difference in BST -> Python3

'''
Explanation: Set lis as empty array and call dfs with root finally returning the min of y - x for 
x,y in zip of lis and lis from 1. Inside dfs do inorder traversal and append node val in lis call 
dfs left if it exists before and call right after append.
'''

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lis = []
        def dfs(node):
            if node.left: dfs(node.left)
            lis.append(node.val)
            if node.right: dfs(node.right)
        dfs(root)
        return min(y - x for x, y in zip(lis, lis[1:]))