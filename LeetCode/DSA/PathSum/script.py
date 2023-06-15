# Path Sum -> Python3

'''
Explanation: If root does not exist return False. If root left and root right are non existent and 
targetsum - root val is 0 then return true. At end return recursive call to same function of root 
left or root right with targetsum - root val.
'''

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None: return False
        if root.left is None and root.right is None and targetSum - root.val == 0: return True
        return self.hasPathSum(root.left,targetSum - root.val) or \
        self.hasPathSum(root.right,targetSum - root.val)