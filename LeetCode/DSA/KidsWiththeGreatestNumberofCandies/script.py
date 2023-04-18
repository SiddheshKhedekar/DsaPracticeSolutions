# Kids With the Greatest Number of Candies -> Python3

'''
Explanation: Set check as the difference between max value in candies and the extracandies. The 
return array where candy is greater than or same as check for each candy in candies.
'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        check = max(candies) - extraCandies
        return [cndy >= check for cndy in candies]