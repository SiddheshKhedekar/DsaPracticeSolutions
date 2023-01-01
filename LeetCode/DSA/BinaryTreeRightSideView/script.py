# Binary Tree Right Side View -> Python3

'''
Explanation: Write a collect function and in it check if depth is len of array and append val. Then 
call the right side collect and then same for left increment the depth in function call.
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def collect(node, depth):
            if node:
                if depth == len(view): view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view