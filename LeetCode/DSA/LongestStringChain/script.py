# Longest String Chain -> Python3

'''
Explanation: Set dp as dict and then loop on sorted words based on len using wrd. Then set dp at 
wrd as the max of dp get of word without char at idx where idx is looped from len range wrd.
'''

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for wrd in sorted(words, key=len):
            dp[wrd] = max(dp.get(wrd[:idx] + wrd[idx + 1:], 0) + 1 for idx in range(len(wrd)))
        return max(dp.values())