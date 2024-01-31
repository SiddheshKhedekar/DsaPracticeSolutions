# Two Sum IV - Input is a BST -> Python3

'''
Explanation: In main function return call to dfs where new set is passed along with target. In dfs 
function check if root is none and return false. Below get the value of target - root value in 
temp. Check if temp present in checked and return true. Add root value in set and return the or of 
root left and right call.
'''

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool: return self.dfs(root, set(), k)
    def dfs(self, root, checked, k):
        if root is None: return False
        temp = k - root.val
        if temp in checked: return True
        checked.add(root.val)
        return self.dfs(root.left, checked, k) or self.dfs(root.right, checked, k)