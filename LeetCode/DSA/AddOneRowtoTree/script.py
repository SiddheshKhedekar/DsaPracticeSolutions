# Add One Row to Tree -> Python3

'''
Explanation: Set temp and temp.left to Treenode(none) and root and set res to array consisting 
temp. In for loop run for range(depth-1) populate res array using [i for nod in res for i in nod 
(left, right) if i]. After loop set another loop for nod in res and set nod.left to Treenode(val) 
and set the nod.left.left to nod.left. The same for right and finally return temp left.
'''

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        temp, temp.left = TreeNode(None), root
        res = [temp]
        for _ in range(depth-1): res = [i for nod in res for i in (nod.left, nod.right) if i]
        for nod in res:
            nod.left, nod.left.left = TreeNode(val), nod.left
            nod.right, nod.right.right = TreeNode(val), nod.right
        return temp.left