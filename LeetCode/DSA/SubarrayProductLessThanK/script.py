# Subarray Product Less Than K -> Python3

'''
Explanation: Use two pointers and run a for loop on the second. Get product by multiplying y value 
and run loop on product with checks and then update product, increment first pointer and at loop 
end update counter.
'''

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, product, counter = 0, 1, 0
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k and l <= r:
                product /= nums[l]
                l += 1
            counter += r - l + 1
        return counter