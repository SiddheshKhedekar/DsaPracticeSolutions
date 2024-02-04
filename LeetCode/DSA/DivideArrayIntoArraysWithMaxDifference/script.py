# Divide Array Into Arrays With Max Difference -> Python3

'''
Explanation: Set res as empty array and l as len nums then sort nums. Then run loof from 0 to l in 
steps of three and set x, y, z as items from indx to its next 2. Check if the difference between 
first and last item is within limit and append the items to res otherwise clear res and return res 
also after loop end return res.
'''

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res, l = [], len(nums)
        nums.sort()
        for indx in range(0, l, 3):
            x, y, z = nums[indx : indx + 3]
            if z - x <= k: res.append([x, y, z])
            else:
                res.clear()
                return res
        return res