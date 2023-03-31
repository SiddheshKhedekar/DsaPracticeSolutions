# Set Mismatch -> Python3

'''
Explanation: Solved using math where n is len nums, a is the -sum of nums + n(n+1)//2 and b is the 
-sum of square of values in nums + n(n+1)(2n+1)//6. Finally return [(B-A*A)//2//A, (B+A*A)//2//A].
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        A = -sum(nums) + n*(n+1)//2
        B = -sum(i*i for i in nums) + n*(n+1)*(2*n+1)//6
        return [(B-A*A)//2//A,(B+A*A)//2//A]