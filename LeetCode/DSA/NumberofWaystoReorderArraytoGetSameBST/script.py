# Number of Ways to Reorder Array to Get Same BST -> Python3

'''
Explanation: Inside func separate list into two lists one less than and other greater than root. 
Then return the comb of len l + len r with len r after multiplying func call for l and r to it. In 
main function return the func of nums - 1 modulo by given value.
'''

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def func(nums):
            if len(nums) <= 2: return 1
            l = [x for x in nums if x < nums[0]]
            r = [x for x in nums if x > nums[0]]
            return comb(len(l) + len(r), len(r)) * func(l) * func(r)
        return (func(nums) - 1) % (10 ** 9 + 7)