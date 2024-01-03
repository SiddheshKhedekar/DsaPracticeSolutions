# Convert an Array Into a 2D Array With Conditions -> Python3

'''
Explanation: Set cnt as counter of nums then mx as max cnt values and temp as list of snt elements 
finally return the array of arrays from temp x to end in steps of mx by looping in range of mx.
'''

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cnt = Counter(nums)
        mx, temp = max(cnt.values()), list(cnt.elements())
        return [temp[x::mx] for x in range(mx)]