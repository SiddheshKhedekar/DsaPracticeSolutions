# Path Sum III -> Python3

'''
Explanation: Set ans, mem as 0, dict 0: 1 and call dfs with root, targetsum, 0 and mem. In dfs 
function check if root is none to return, then increment curps by root val and set oldps as curps - 
trgt. Increment global ans by mem on get of oldps else 0 and set mem curps after geting mem curps 
else 0 and adding 1 to it. Call dfs left and right passing trgt curps and mem and decrement mem 
curps by 1.
'''

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans, mem = 0, {0: 1}
        def dfs(root, trgt, curPs, mem):
            if root is None: return
            curPs += root.val
            oldPs = curPs - trgt
            self.ans += mem.get(oldPs, 0)
            mem[curPs] = mem.get(curPs, 0) + 1
            dfs(root.left, trgt, curPs, mem)
            dfs(root.right, trgt, curPs, mem)
            mem[curPs] -= 1
        dfs(root, targetSum, 0, mem)
        return self.ans