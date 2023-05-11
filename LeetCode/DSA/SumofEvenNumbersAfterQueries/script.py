# Sum of Even Numbers After Queries -> Python3

'''
Explanation: Save sum of all even numbers. Run loop for i, j in queries. Check if nums[j] is even 
and subtract from sum. Add the i value to nums[j]. Check if nums[j] is even again and add nums[j] 
to sum. Before looping again append the sum to output array.
'''

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(i for i in nums if i%2 == 0)
        out = []
        for i, j in queries:
            if nums[j]%2 == 0: s-=nums[j]
            nums[j]+=i
            if nums[j]%2 == 0: s+=nums[j]
            out.append(s)
        return out