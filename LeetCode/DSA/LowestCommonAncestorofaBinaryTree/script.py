# Lowest Common Ancestor of a Binary Tree -> Python3

'''
Explanation: If root is none or the params then return root and then assign left and right after 
recursive call to child and params where child is the left and right child. Finally return root if 
left and right else return either of them.
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q): return root
        l, r = (self.lowestCommonAncestor(child, p, q) 
                for child in (root.left, root.right))
        return root if l and r else l or r