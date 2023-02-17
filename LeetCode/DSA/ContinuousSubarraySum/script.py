# Continuous Subarray Sum -> Python3

'''
Explanation: Set hashmap to dict 0:0 and s to 0. Run a for loop in range of len nums and add 
nums[i] value to s, then check if s%k remainder is not in hashmap and set hashmap remainder to i+1 
else if hashmap remainder < i then true otherwise false at loop end.
'''

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map, s = {0: 0}, 0
        for i in range(len(nums)):
            s += nums[i]
            if s% k not in hash_map: hash_map[s%k] = i+1
            elif hash_map[s%k] < i: return True
        return False