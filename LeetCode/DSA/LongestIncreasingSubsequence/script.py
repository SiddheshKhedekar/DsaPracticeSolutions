# Longest Increasing Subsequence -> Python3

'''
Explanation: Set ans as empty array and run loop for i in nums. Check if len of ans is 0 or ans at 
end is less than i to append i in ans. Else set idx as bisectleft of ans,i and set ans at idx at i.
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            if len(ans) == 0 or ans[-1] < i: ans.append(i)
            else: idx, ans[idx] = bisect_left(ans, i), i
        return len(ans)