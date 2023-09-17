# Maximum Length of Repeated Subarray -> Python3

'''
Explanation: Use dp. Assign memory using list comprehension having size in both dimension of size 
nums2+1 and nums1+1. Traverse first list in reverse order in for loop and inside traverse the 
second list same as one above. If nums1 i is equal to nums2 j then assign memory i j to 
(memory i +1 j+1)+1. Finally return the max for the max value for each row in memory.
'''

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        mem = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(len(nums1)-1,-1,-1):
            for j in range(len(nums2)-1,-1,-1):
                if nums1[i] == nums2[j]: mem[i][j] = mem[i+1][j+1]+1
        return max(max(row) for row in mem)