# Count Elements With Maximum Frequency -> Python3

'''
Explanation: Set frequencies in first loop then set max in another loop and in third loop get sum 
of max values in res.
'''

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f, mx, res = {}, 0, 0
        for x in nums: f[x] = f.get(x, 0) + 1
        for _, value in f.items(): mx = max(mx, value)
        for _, value in f.items(): 
            if value == mx: res += value
        return res