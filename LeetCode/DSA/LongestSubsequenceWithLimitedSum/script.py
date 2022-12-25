# Longest Subsequence With Limited Sum -> Python3

'''
Explanation: First save the accumulated sum of the sorted list. Then perform binary search on 
queries and return the right side of the array.
'''

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        summ = list(accumulate(sorted(nums)))
        return [bisect_right(summ, q) for q in queries]