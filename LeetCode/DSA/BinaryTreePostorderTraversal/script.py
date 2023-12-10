# Binary Tree Postorder Traversal -> Python3

'''
Explanation: Pass empty array to dfs function. For postorder traversal use check for left child 
first then check for right child and then append root value. Inside check for child call 
recursively to the same function for respective child.
'''

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.dfsposto(root,out)
        return out
    def dfsposto(self,root,out):
        if root is None: return
        if root.left is not None: self.dfsposto(root.left,out)
        if root.right is not None: self.dfsposto(root.right,out)
        out.append(root.val)