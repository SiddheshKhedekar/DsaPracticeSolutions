# Maximum Number of Coins You Can Get -> Python3

'''
Explanation: First the piles need to be sorted then give the smallest values Bob, give the biggest 
to Alice, and leave the second biggest to us. Following this pattern we can eliminate a third of 
the array and then take the sum of every element left in array with skip of 2.
'''

class Solution:
    def maxCoins(self, piles: List[int]) -> int: return sum(sorted(piles)[len(piles) // 3::2])