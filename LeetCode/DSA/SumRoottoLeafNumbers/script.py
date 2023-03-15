# Sum Root to Leaf Numbers -> Python3

'''
Explanation: The result is given by dfs call to root and 0. Inside dfs function check for not root 
and return 0 then set current to current * 10 plus root val. If not root left and not right then 
return current otherwise return dfs root left and right call along with current.
'''

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, current):
            if not root: return 0
            current = current * 10 + root.val
            if not root.left and not root.right: return current
            return dfs(root.left, current) + dfs(root.right, current)
        return dfs(root, 0)