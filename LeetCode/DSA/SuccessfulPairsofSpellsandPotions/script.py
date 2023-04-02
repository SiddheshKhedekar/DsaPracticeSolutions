# Successful Pairs of Spells and Potions -> Python3

'''
Explanation: Save length of spells, potions in x, y and ans as array of 0 of size x then sort 
potions. Run for loop on x and set spell ac current spell, l as 0 and r as y minus 1. Then run 
binary search in while loop unitl product greater than success and at end set ans at i as y - 1.
'''

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        x, y = len(spells), len(potions)
        ans = [0] * x
        potions.sort()
        for i in range(x):
            spell, l, r = spells[i], 0, y - 1
            while l <= r:
                mid = l + (r - l) // 2
                product = spell * potions[mid]
                if product >= success: r = mid - 1
                else: l = mid + 1
            ans[i] = y - l
        return ans