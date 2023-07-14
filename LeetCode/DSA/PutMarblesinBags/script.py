# Put Marbles in Bags -> Python3

'''
Explanation: Set newWeights as array of x + y for all x, y in pairwise weights then return the sum 
of nlargest k-1, newWeights after subtracting sum of nsmallest k-1, newWeights.
'''

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        newWghts = [x + y for x, y in pairwise(weights)]
        return sum(nlargest(k - 1, newWghts)) - sum(nsmallest(k - 1, newWghts))