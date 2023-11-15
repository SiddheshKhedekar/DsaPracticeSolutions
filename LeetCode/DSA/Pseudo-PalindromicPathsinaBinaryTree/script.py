# Pseudo-Palindromic Paths in a Binary Tree -> Python3

'''
Explanation: Initialize count to 0 defined a subfunction to which node and path is passed define 
nonlocal count again. Check if node and inside set path to path ^ (1<< node.val). If node both 
children are none then check if path & (path-1) ==0 and increment count by 1 else run preorder 
function call twice once for left and once for right. In main function call preorder function 
passing root and 0 and return count.
'''

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        count = 0
        def preorder(node, path):
            nonlocal count
            if node:
                path = path ^ (1 << node.val)
                if node.left is None and node.right is None:
                    if path & (path-1) == 0: count+=1
                else:
                    preorder(node.left,path)
                    preorder(node.right,path)
        preorder(root,0)
        return count