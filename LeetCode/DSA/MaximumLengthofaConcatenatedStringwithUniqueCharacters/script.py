# Maximum Length of a Concatenated String with Unique Characters -> Python3

'''
Explanation: Define dp as array of set and run a for loop on arr. Check if len set a < than len a 
and continue change a to set a and run for again in dp[:] check if a & c and continue otherwise do 
dp.append a|c and outside both for return max len a in dp.
'''

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a): continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)