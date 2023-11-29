# Sum of Absolute Differences in a Sorted Array -> Python3

'''
Explanation: Set lsum as 0, rsum as sum nums, res as array and l as len of nums. Then loop on the 
enumerated nums with x, n and inside append into ans the simplified version of the equation and 
increment lsum by n while decrementing rsum by it. The equation for abs diff of elements can be 
evaluated as n * x - lsum + rsum - (1 - x) * n finally return ans at end.
'''

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        lsum, rsum, ans, l = 0, sum(nums), [], len(nums)
        for x, n in enumerate(nums):
            ans.append(x * n - lsum + rsum - (l - x) * n)
            lsum += n
            rsum -= n
        return ans