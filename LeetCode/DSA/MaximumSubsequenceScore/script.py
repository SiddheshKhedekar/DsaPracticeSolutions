# Maximum Subsequence Score -> Python3

'''
Explanation: Set tot, ans, hp as 0, 0, [] and run loop for x, y in sorted list zip of nums1, nums2 
where key is lambda xy: -xy at 1. Inside peappushx in hp then increment tot by x. Check if len hp 
is greater than k to decrement tot by heappop of hp and check if len hp is same as k to set ans as 
max of ans and tot * y.
'''

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        tot, ans, hp = 0, 0, []
        for x, y in sorted(list(zip(nums1, nums2)), key=lambda xy: -xy[1]):
            heappush(hp, x)
            tot += x
            if len(hp) > k: tot -= heappop(hp)
            if len(hp) == k: ans = max(ans, tot * y)
        return ans