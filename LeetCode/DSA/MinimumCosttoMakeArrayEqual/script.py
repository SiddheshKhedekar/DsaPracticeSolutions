# Minimum Cost to Make Array Equal -> Python3

'''
Explanation: Assuming the final equal values are x the total cost function is a convex function on 
the range of min, max of nums. To find the minimum value of func, we can binary search x by 
comparing func for mid and mid + 1. If func for mid is less than for mid + 1, the minimum func is 
on the left of mid, where x less than mid. If func for mid is greater than or same as for mid + 1, 
the minimum func is on the right of mid + 1, where x greater than or same as mid. We need to 
again do this while left less than right, until we find the minimum value and return it. This 
method is known as trinary search, if we check func for mid and mid2.
'''

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def func(i): return sum(abs(num - i) * c for num, c in zip(nums, cost))
        left, right = min(nums), max(nums)
        res = func(left)
        while left < right:
            i = (left + right) // 2
            j1, j2 = func(i), func(i + 1)
            res = min(j1, j2)
            if j1 < j2: right = i
            else: left = i + 1
        return res