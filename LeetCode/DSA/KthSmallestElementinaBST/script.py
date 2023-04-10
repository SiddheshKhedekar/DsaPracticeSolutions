# Kth Smallest Element in a BST -> Python3

'''
Explanation: Initialize stack and run loop while root or stack exist. Then run loop while root 
exists to append root to stack and set root to its left. End inner loop, set root to stack pop and 
decrement k by 1 then check if k is 0 to return root val otherwise set root to its right.
'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        while root or stk:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            k -= 1
            if k == 0: return root.val
            root = root.right