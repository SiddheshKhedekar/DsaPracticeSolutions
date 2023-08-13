# Make Array Strictly Increasing -> Python3

'''
Explanation: Set dp as dict with value 0 at key -1 then sort arr2 and run for loop on x in arr1. 
Inside set temp as defaultdict of lambda float inf and run another for loop on key in dp. Check if 
x is less than key and set temp at x as the min of itself and dp at key then get loc after bisect 
right on arr2, key. Check if loc is less than len of arr2 and set temp at arr2 loc as min of itself 
and dp at key + 1. Outside inner loop set dp as temp and check if dp to return the min of dp values 
otherwise return -1.
'''

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = {-1: 0}
        arr2.sort()
        for x in arr1:
            temp = defaultdict(lambda: float('inf'))
            for key in dp:
                if x > key: temp[x] = min(temp[x], dp[key])
                loc = bisect_right(arr2, key)
                if loc < len(arr2): temp[arr2[loc]] = min(temp[arr2[loc]], dp[key] + 1)
            dp = temp
        if dp: return min(dp.values())
        return -1