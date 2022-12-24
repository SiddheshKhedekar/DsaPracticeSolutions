# Leaf-Similar Trees -> Python3

'''
Explanation: Use a dfs function to iterate both trees and check if all notes are equal.
'''

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return
            if not node.left and not node.right: yield node.val
            for i in dfs(node.left): yield i
            for i in dfs(node.right): yield i
        return all(a == b for a, b in itertools.zip_longest(dfs(root1),dfs(root2)))