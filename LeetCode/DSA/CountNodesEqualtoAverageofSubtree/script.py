# Count Nodes Equal to Average of Subtree -> Python3

'''
Explanation: In main function initialize res as 0 then call dfs on root and return res. In dfs set 
nonlocal res and if node not valid then return 0, 0. Maintain lsum, lcnt and rsum, rcnt by dfs call 
to left and right child of node. Set sm as the sum of node.val, lsum, rsum and cnt sum of 1, lcnt, 
rcnt then check if average is node val to return sm, cnt
'''

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node: return 0, 0
            lSum, lCnt = dfs(node.left)
            rSum, rCnt = dfs(node.right)
            sm = node.val + lSum + rSum
            cnt = 1 + lCnt + rCnt
            if sm // cnt == node.val: res += 1
            return sm, cnt
        dfs(root)
        return res