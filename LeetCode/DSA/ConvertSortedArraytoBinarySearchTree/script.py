# Convert Sorted Array to Binary Search Tree -> Python3

'''
Explanation: Save len and if not l return none then set m to len floor divide by 2. Return the 
Treenode cast of nums[m], recursive call to function for nums[:m] and same for nums[m+1:].
'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l = len(nums)
        if not l: return None
        m = l // 2
        return TreeNode(nums[m],self.sortedArrayToBST(nums[:m]),self.sortedArrayToBST(nums[m+1:]))