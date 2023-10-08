# Maximum Level Sum of a Binary Tree -> Python3

'''
Explanation: Initialise res, que, dpt as set of -inf and 0, array of root , -1 then run loop while 
que. Inside set res as max of res and  sum of node val for all nodes in que, dpt. Then set que as 
array of kid for node in que and for kid in node left, right if kid exists. Decrement dept by one 
and outside of loop return the negative of res at 1.
'''

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res, que, dpt = (-math.inf, 0), [root], -1
        while que:
            res = max(res, (sum(node.val for node in que), dpt))
            que = [kid for node in que for kid in (node.left, node.right) if kid]
            dpt -= 1
        return -res[1]