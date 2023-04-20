# Longest ZigZag Path in a Binary Tree -> Python3

'''
Explanation: We define dfs function to return the max length in left direction, right direction and 
the whole subtree. Inside dfs function if not root then return array of three -1, set l as 
recursive call to root left and similarly r as recursive call to root right. Then return the array 
where l is l at index 1 + 1, r is r at index 0 + 1 and res as max of the earlier 2 values along 
with the results for l and r. In main func return the last value in call to dfs.
'''

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return [-1, -1, -1]
            l, r = dfs(root.left), dfs(root.right)
            return [l[1] + 1, r[0] + 1, max(l[1] + 1, r[0] + 1, l[2], r[2])]
        return dfs(root)[-1]