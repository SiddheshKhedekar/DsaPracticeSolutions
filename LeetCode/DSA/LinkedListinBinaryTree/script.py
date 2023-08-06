# Linked List in Binary Tree -> Python3

'''
Explanation: Implement kmp search. Iterate the head and find the max matched length of prefix then 
save it as items in dp then call dfs on root, 0. In dfs iterate for root and find max length of 
prefix, check if x is len of dp or dfs call to what either of the child, x return.
'''

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        arr, dp, x, node = [head.val], [0], 0, head.next
        while node:
            while x and node.val != arr[x]: x = dp[x - 1]
            x += node.val == arr[x]
            arr.append(node.val)
            dp.append(x)
            node = node.next
        def dfs(root, x):
            if not root: return False
            while x and root.val != arr[x]: x = dp[x - 1]
            x += root.val == arr[x]
            return x == len(dp) or dfs(root.left, x) or dfs(root.right, x)
        return dfs(root, 0)