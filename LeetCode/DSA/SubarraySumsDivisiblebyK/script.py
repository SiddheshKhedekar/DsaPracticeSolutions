# Subarray Sums Divisible by K -> Python3

'''
Explanation: Get the running sums mod by k and increment frequency after adding to final count.
'''

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans, rsum, cnt = 0, 0, [1] + [0] * k
        for num in nums:
            rsum = (rsum + num) % k
            ans += cnt[rsum]
            cnt[rsum] += 1
        return ans