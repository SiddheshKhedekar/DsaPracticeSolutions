# Construct Binary Tree from Preorder and Inorder Traversal -> Python3

'''
Explanation: Check if inorder exists and set i to the index of preorder pop 0 in inorder. Set root 
to treenode of inorder index and recursively call for left and right passing preorder as is and 
inorder up to index for left and after index to right.
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if inorder:
            i = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[i])
            root.left = self.buildTree(preorder, inorder[0:i])
            root.right = self.buildTree(preorder, inorder[i + 1:])
            return root