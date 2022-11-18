# Same Tree -> Python3

'''
Explanation: If both trees end then then they are same. If any one tree end then they are not same 
and also not same if tree values dont match. Recursive call to rights and lefts of both trees.
'''

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        return self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)