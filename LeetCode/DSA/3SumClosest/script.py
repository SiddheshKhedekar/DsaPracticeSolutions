# 3Sum Closest -> Python3

'''
Explanation: Sort nums and in result save the sum of first 3 nums. Run for loop on range len nums-2 
and check if i >0 and nums[i] = nums[i-1] then continue. Set j, k to i+1, len nums-1. Run while 
j < k loop and set sum to sum nums i j and k. If sum = target return sum, if abs sum-target < abs 
result-target set result to sum. If sum< target increment j by 1 elseif sum > target decrement k by 
1. Finally return result.
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = sum(nums[:3])
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            j, k = i+1, len(nums)-1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == target: return summ
                if abs(summ - target) < abs(result - target): result = summ
                if summ < target: j+=1
                elif summ > target: k-=1
        return result