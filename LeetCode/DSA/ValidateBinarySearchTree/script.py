# Validate Binary Search Tree -> Python3

'''
Explanation: Recursive solution possible but for simplicity using inorder traversal function 
getting the array and comparing if any previous element is greater than or equal to the current 
one. If the condition meets then it is not bst.
'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        out = []
        self.dfsio(root,out)
        for i in range(1,len(out)):
            if out[i-1] >= out[i]: return False
        return True
    
    def dfsio(self,root,out):
        if root is None: return
        self.dfsio(root.left,out)
        out.append(root.val)
        self.dfsio(root.right,out)