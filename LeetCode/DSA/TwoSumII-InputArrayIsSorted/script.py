# Two Sum II - Input Array Is Sorted -> Python3

'''
Explanation: For i in range lo array nums len set l as i+1 and r as len nums -1. Set temp as 
target - nums[i]. Run while loop for l <= r. Set m to l+(r-l)//2 and check if nums[m] == temp then 
return [i-1,m+1] elseif nums[m] < temp then l = m+1 else r = m-1.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i+1, len(numbers)-1
            tmp =  target - numbers[i]
            while l <= r:
                m = l + (r-l)//2
                if numbers[m] == tmp: return [i+1,m+1]
                elif numbers[m] < tmp: l = m+1
                else: r = m-1