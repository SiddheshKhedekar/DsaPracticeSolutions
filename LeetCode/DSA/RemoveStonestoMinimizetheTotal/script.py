# Remove Stones to Minimize the Total -> Python3

'''
Explanation: Create min heap from piles and then iteration on k replace the heap by its floor 
division finally return the sum.
'''

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-a for a in piles]
        heapq.heapify(piles)
        for i in range(k):
            heapq.heapreplace(piles,piles[0]//2)
        return -sum(piles)