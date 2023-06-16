# Maximum Depth of Binary Tree -> Python3

'''
Explanation: Use a recursive dfs function to which depth is passed. Inside dfs function if no next 
node present then return depth outside return the max of dfs function for left and right with depth 
increased by one.
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: return self.dfsd(root,0)
    def dfsd(self,root,depth):
        if root is None: return depth
        return max(self.dfsd(root.left,depth+1),self.dfsd(root.right,depth+1))