# Contains Duplicate II -> Python3

'''
Explanation: Use memory dictonary to save the index in dictonary where key is the number in array 
when running for loop. Check if number in dictonary for duplication and number is nearby and return 
true finally return false.
'''

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, j in enumerate(nums):
            if j in dic and i - dic[j] <= k: return True
            dic[j] = i
        return False