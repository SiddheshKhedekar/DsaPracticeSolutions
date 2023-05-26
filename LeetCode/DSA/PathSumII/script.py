# Path Sum II -> Python3

'''
Explanation: Initialize out as empty array and call dfs function with root, targetsum, empty array 
and out. Inside the dfs function check if root then check if not root left and not root right and 
targetsum is same as root val to append root val to l and append l to out. Recursively call the 
left and right root with targetsum-root val, l + root val as array and out.
'''

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        out = []
        self.dfs(root,targetSum,[],out)
        return out 
    def dfs(self, root, targetSum, l, out):
        if root:
            if not root.left and not root.right and targetSum == root.val:
                l.append(root.val)
                out.append(l)
            self.dfs(root.left,targetSum-root.val,l+[root.val],out)
            self.dfs(root.right,targetSum-root.val,l+[root.val],out)