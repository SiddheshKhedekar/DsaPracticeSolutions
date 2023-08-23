# Number of Longest Increasing Subsequence -> Python3

'''
Explanation: Check if nums invalid and return 0 then set l as len nums + 1. Initialise dck, 
end_dcks, pths as array of arrays, array with inf and array with arrayitem 0 all 3 of length l. Run 
loop of n in nums and inside set idx as bisect left of end_dcks, n and n_paths as 1. Check if idx 
is greater than 0 and set l as bisect of dcks at idx -1 , -n then set n_pths as pths at idx - 1, -1 
after subtracting pths at idx -1, l. Outside if condition append -n in dcks at idx then sed n at 
idx in end_dcks and append n_pths + pths at idx, -1 into pths at idx. Finally return the pths at 
pths index 0 after subtracting 1, -1.
'''

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        l = len(nums) + 1
        dcks, end_dcks, pths = [[] for _ in range(l)], [float('inf')] * l, [[0] for _ in range(l)]
        for n in nums:
            idx, n_pths = bisect_left(end_dcks, n), 1
            if idx > 0:
                l = bisect.bisect(dcks[idx - 1], -n)
                n_pths = pths[idx - 1][-1] - pths[idx - 1][l]
            dcks[idx].append(-n)
            end_dcks[idx] = n
            pths[idx].append(n_pths + pths[idx][-1])
        return pths[pths.index([0]) - 1][-1]