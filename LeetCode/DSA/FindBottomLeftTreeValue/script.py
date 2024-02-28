# Find Bottom Left Tree Value -> Python3

'''
Explanation: Set q as array of root then loop for nodes in q to append the child node if exists to 
q and return node value at end of loop.
'''

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = [root]
        for n in q: q += filter(None, (n.right, n.left))
        return n.val