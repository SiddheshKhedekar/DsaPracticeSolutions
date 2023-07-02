# Maximum Number of Achievable Transfer Requests -> Python3

'''
Explanation: Run loop on range of len requests to 0 as i and inside run loop on combinations of 
requests, i as z. Check for counter x matches that of y and return i otherwise return 0.
'''

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        for i in range(len(requests), 0, -1):
            for z in combinations(requests, i):
                if Counter(x for x, y in z) == Counter(y for x, y in z):  return i
        return 0