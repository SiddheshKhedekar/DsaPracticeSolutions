# Construct String from Binary Tree -> Python3

'''
Explanation: Use recursion of the same function First return if not not existing. Then check if 
left or right node exists. Use recursion passing left node along with the needed formatting. Below 
add another condition only for right node check and do the same for right. Finally string append 
the result and return.
'''

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None: return ''
        if root.left is not None or root.right is not None: left = '('+self.tree2str(root.left)+')'
        else: left = ''
        if root.right is not None: right = '('+self.tree2str(root.right)+')'
        else: right = ''
        return str(root.val)+left+right