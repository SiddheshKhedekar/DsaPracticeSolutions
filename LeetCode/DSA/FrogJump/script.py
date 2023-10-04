# Frog Jump -> Python3

'''
Explanation: Use backtracking using dfs and update seen. First set seen as set, trgt as stones at 
last index and stones as the set of stones then return the dfs call using stones, 1, 1, trgt. In 
dfs check if the set of crnt and spd are in seen to return false then check if crnt is trgt to 
return true. Check if crnt is greater than trgt or crnt is less than 0 or spd is less than or same 
as 0 or crnt is not in stones to return false. Then loop on spd and its neighbors before and after, 
inside check if crnt + i is in stones to again check if dfs of stones, crnt + i, i, trgt to return 
true. Outside loop add crnt, spd in seen and return false.
'''

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        self.seen, trgt, stones = set(), stones[-1], set(stones)
        return self.dfs(stones, 1, 1, trgt)
    def dfs(self, stones, crnt, spd, trgt):
        if (crnt, spd) in self.seen: return False
        if crnt == trgt: return True
        if crnt > trgt or crnt < 0 or spd <= 0 or crnt not in stones: return False
        for i in [spd - 1, spd, spd + 1]:
            if (crnt + i) in stones:
                if self.dfs(stones, crnt + i, i, trgt): return True
        self.seen.add((crnt, spd))
        return False