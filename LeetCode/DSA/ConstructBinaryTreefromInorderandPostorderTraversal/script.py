# Construct Binary Tree from Inorder and Postorder Traversal -> Python3

'''
Explanation: Map inorder in a dict and set val to index in loop then return call to function with 0 
and len-1. Inside function set node with postorder pop and mid with dict node val. Set left and 
right with recursive call and return node.
'''

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {}
        for index, value in enumerate(inorder): inorder_map[value] = index
        def func(start, end):
            if start > end: return None
            node = TreeNode(postorder.pop())
            mid = inorder_map[node.val]
            node.right = func(mid + 1, end)
            node.left = func(start, mid - 1)
            return node
        return func(0, len(inorder) - 1)