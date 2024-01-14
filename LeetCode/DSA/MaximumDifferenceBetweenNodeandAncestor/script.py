# Maximum Difference Between Node and Ancestor -> Python3

'''
Explanation: Set default params mind and maxd as upper and lower range. Inside function return the 
max of root left and right with min and max between mind maxd and root val respectively if root 
exists else return maxd - mind.
'''

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode], minD = 100000, maxD = 0) -> int:
        return max(self.maxAncestorDiff(root.left, min(minD, root.val), max(maxD, root.val)), \
                    self.maxAncestorDiff(root.right, min(minD, root.val), max(maxD, root.val))) \
                    if root else maxD - minD