# Even Odd Tree -> Python3

'''
Explanation: Set q to deque of root as array and use while for level incrementing then for loop to 
check if the level and number of children match.
'''

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        q, l = deque([root]), 0
        while q:
            pv = None
            for _ in range(len(q)):
                n = q.popleft()
                if (l % 2 == 0 and (n.val % 2 == 0 or \
                (pv is not None and n.val <= pv))) or \
                (l % 2 == 1 and (n.val % 2 == 1 or \
                (pv is not None and n.val >= pv))): return False
                pv = n.val
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            l += 1
        return True