# Poor Pigs -> Python3

'''
Explanation: We can solve up to 25 buckets in 60 mins with 2 pigs and poison taking 15 mins to 
kill. Similarly we can solve 125 buckets with 3 pigs and we can generalise this equation as 
(testtime / killtime + 1) to the power of no of pigs. Use a while loop to increment no of pigs by 1 
till the condition value is less than buckets.
'''

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pgs = 0
        while (minutesToTest / minutesToDie + 1) ** pgs < buckets: pgs += 1
        return pgs