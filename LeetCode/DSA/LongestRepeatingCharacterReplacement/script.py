# Longest Repeating Character Replacement -> Python3

'''
Explanation: Set l, lsl and freq to 0, 0 and defaultdict int after that run a for loop in range len 
s and increment freq[s[i]] by 1. Set cc to i -l +1 and then check if cc - max(freq.values) <= k and 
set lsl to max lsl and cc. In else decrement freq[s[l]] by 1 and increment l by 1 at end return lsl.
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, lsl, freq = 0, 0, defaultdict(int)
        for i in range(len(s)):
            freq[s[i]] += 1
            cc = i - l + 1
            if cc - max(freq.values()) <= k: lsl = max(lsl, cc)
            else:
                freq[s[l]] -= 1
                l += 1
        return lsl