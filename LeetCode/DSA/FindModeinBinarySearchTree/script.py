# Find Mode in Binary Search Tree -> Python3

'''
Explanation: Set global pre, mxCnt, curCnt, ans as none, 0, 0, new array. In main function call dfs 
with root and return ans. In dfs check if root invalid and return, then call dfs on root left. Set 
curCnt as 1 if node.val is not pre else increment curCnt by 1. Check if curCnt is mxCnt to append 
node val in ans else if curCnt is greater than mxCnt then set ans as the node val as array and 
update mxCnt as curCnt. Set pre as node val and call dfs on node right.
'''

class Solution:
    pre, mxCnt, curCnt, ans = None, 0, 0, []
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.ans
    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        self.curCnt = 1 if node.val != self.pre else self.curCnt + 1
        if self.curCnt == self.mxCnt: self.ans.append(node.val)
        elif self.curCnt > self.mxCnt: self.ans, self.mxCnt = [node.val], self.curCnt
        self.pre = node.val
        self.dfs(node.right)