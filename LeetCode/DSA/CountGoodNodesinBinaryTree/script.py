# Count Good Nodes in Binary Tree -> Python3

'''
Explanation: Write a dfs function and pass the root and current max to it. Increment count when 
condition is met and call the children nodes.
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        def dfs(node,curMax):
            if not node: return
            if node.val >= curMax:
                count[0] += 1
                curMax = node.val
            dfs(node.left, curMax)
            dfs(node.right, curMax)
        count = [0]
        dfs(root,root.val)
        return count[0]