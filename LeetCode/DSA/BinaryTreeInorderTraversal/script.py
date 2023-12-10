# Binary Tree Inorder Traversal -> Python3

'''
Explanation: Pass empty array to dfs function. For inorder traversal use check for left child first 
then append root value and then check for right child. Inside check for child call recursively to 
the same function for respective child.
'''

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.dfsio(root,out)
        return out
    def dfsio(self,root,out):
        if root is None: return
        if root.left is not None: self.dfsio(root.left,out)
        out.append(root.val)
        if root.right is not None: self.dfsio(root.right,out)