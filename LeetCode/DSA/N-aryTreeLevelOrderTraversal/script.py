# N-ary Tree Level Order Traversal -> Python3

'''
Explanation: Write a dfs function that takes in root and level. If root is none then return, if 
level is length array then append empty array to result. At level append root value in array. For 
all children do dfs call with increment in level.
'''

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(root, level):
            if root == None: return
            if level == len(ans): ans.append([])
            ans[level].append(root.val)
            for child in root.children: dfs(child, level+1)
        ans = []
        dfs(root, 0)
        return ans