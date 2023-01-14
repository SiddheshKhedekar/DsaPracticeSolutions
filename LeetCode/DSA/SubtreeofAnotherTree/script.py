# Subtree of Another Tree -> Python3

'''
Explanation: Write a function to check if root and subroot match. Call it for the main params and 
check and also check if root exists. Return the recursive call for left or right part of tree. 
Inside match function check if  not both root and subroot and return root is subroot otherwise 
return after checking the values and is match for left and right.
'''

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatch(r, sr):
            if not(r and sr): return r is sr
            return (r.val == sr.val and isMatch(r.left, sr.left) and isMatch(r.right, sr.right))
        if isMatch(root, subRoot): return True
        if not root: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)