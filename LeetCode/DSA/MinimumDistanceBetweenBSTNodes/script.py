# Minimum Distance Between BST Nodes -> Python3

'''
Explanation: Set pre and res to min and max values outside of function call. As long as left child 
exists recursive call for the node. Set res to min of res and current val minus pre and then set 
pre to val. Finally, call recursively for the right child and at end of flow we have result in res.
'''

class Solution:
    pre, res = -float('inf'), float('inf')
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root.left: self.minDiffInBST(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val
        if root.right: self.minDiffInBST(root.right)
        return self.res