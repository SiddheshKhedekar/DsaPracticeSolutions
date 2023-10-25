# Find Largest Value in Each Tree Row -> Python3

'''
Explanation: Set mx as new array and r as array of root. Then run loop while any r, inside append 
the max of node val for all nod in r into mx and set r as the array of child for node in r and 
child in node left, right if child is valid. At end of loop return mx.
'''

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        mx, r = [], [root]
        while any(r):
            mx.append(max(nod.val for nod in r))
            r = [child for nod in r for child in (nod.left, nod.right) if child]
        return mx