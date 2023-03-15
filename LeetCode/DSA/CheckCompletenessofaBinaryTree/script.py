# Check Completeness of a Binary Tree -> Python3

'''
Explanation: For a full tree we need x = 2^k - 1 nodes and for x by property we can check same with 
x & (x+1) equals 0. We implement the same in dfs condition for left and right along with the 
respective subtree node count condition after recursive call to children and return l + r + 1. Then 
check if dfs returns greater than 0.
'''

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            if left & (left + 1) == 0 and left / 2 <= right <= left: return left + right + 1
            if right & (right + 1) == 0 and right <= left <= right * 2 + 1: return left + right + 1
            return -1
        return dfs(root) > 0