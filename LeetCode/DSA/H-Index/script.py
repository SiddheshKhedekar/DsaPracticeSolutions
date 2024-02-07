# H-Index -> Python3

'''
Explanation: First we need to sort the citations in reverse then enumerate on it calculate the sum 
if its index is less than value.
'''

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(x < y for x, y in enumerate(sorted(citations, reverse = True)))