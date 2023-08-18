# Sliding Window Maximum -> Python3

'''
Explanation: Set que as deque and ans as empty array then run loop for index and crnt element in 
enumerated nums. Inside run loop while que and nums at last element in q is less than or same as 
crnt to pop que. Append the index in que and check if que at start is index - k to pop left from 
que then check if index is greater than or same as k - 1 to append nums at que 0 in ans.
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que, ans = deque(), []
        for indx, crnt in enumerate(nums):
            while que and nums[que[-1]] <= crnt: que.pop()
            que.append(indx)
            if que[0] == indx - k: que.popleft()
            if indx >= k - 1: ans.append(nums[que[0]])
        return ans