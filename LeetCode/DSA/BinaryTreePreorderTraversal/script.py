# Binary Tree Preorder Traversal -> Python3

'''
Explanation: Pass empty array to dfs function. For preorder traversal append root value first then 
use check for left child and then check for right child. Inside check for child call recursively to 
the same function for respective child.
'''

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        self.dfspreo(root,out)
        return out
    def dfspreo(self,root,out):
        if root is None: return
        out.append(root.val)
        if root.left is not None: self.dfspreo(root.left,out)
        if root.right is not None: self.dfspreo(root.right,out)