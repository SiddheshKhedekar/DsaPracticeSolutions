# Count Number of Homogenous Substrings -> Python3

'''
Explanation: Set ans as 0 then loop on index and itertools list s created by group by on s. Set len 
of s in l and increment ans by l * l+1 after floor div by 2. At end return ans mod by given value.
'''

class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = 0
        for _, s in groupby(s):
            l = len(list(s))
            ans += l * (l + 1) // 2
        return ans % (10 ** 9 + 7)