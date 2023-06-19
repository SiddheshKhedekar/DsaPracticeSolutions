# N-ary Tree Preorder Traversal -> Python3

'''
Explanation: In main function initialize output call dfs function and return output. In dfs 
function check if root is none return. Append the root value in output. For child in loop of root 
children call dfs function passing child and output.
'''

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        out = []
        self.dfsio(root,out)
        return out
    def dfsio(self,root,out):
        if root is None: return
        out.append(root.val)
        for i in root.children: self.dfsio(i,out)