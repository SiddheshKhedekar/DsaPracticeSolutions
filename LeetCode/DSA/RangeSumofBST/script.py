# Range Sum of BST -> Python3

'''
Explanation: Implement a dfs function to recursively pass the nodes of tree and check if value 
between limits and increment the value of final output.
'''

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node: return
            if low <= node.val <= high: self.out += node.val
            if node.val > low: dfs(node.left)
            if node.val < high: dfs(node.right)
        self.out = 0
        dfs(root)
        return self.out