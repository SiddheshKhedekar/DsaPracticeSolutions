# Combination Sum III -> Python3

'''
Explanation: Set res as array and call dfs function with list of 1 to 10, k, n, empty array and 
res. In dfs check if k and n are valid then check if k and n are 0 to append route in res. Run loop 
for x in len nums and inside call dfs with nums x+ 1 to end, k - 1, n - nums at x, route at num at 
x and res.
'''

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(nums, k, n, route, res):
            if k < 0 or n < 0: return
            if k == 0 and n == 0: res.append(route)
            for x in range(len(nums)):
                dfs(nums[x + 1:], k - 1, n - nums[x], route + [nums[x]], res)
        dfs(list(range(1, 10)), k, n, [], res)
        return res