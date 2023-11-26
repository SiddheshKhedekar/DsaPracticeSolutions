# Diagonal Traverse II -> Python3

'''
Explanation: Set ans ar array and loop on x, num in enumerated nums then loop again for y, n in 
enumerated num. Inside check if len ans is less than or same as x + y to append array in ans then 
append n at x + y in ans. Finally return the array of n in reversed num for each num in ans.
'''

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for x, num in enumerate(nums):
            for y, n in enumerate(num):
                if len(ans) <= x + y: ans.append([])
                ans[x + y].append(n)
        return [n for num in ans for n in reversed(num)]