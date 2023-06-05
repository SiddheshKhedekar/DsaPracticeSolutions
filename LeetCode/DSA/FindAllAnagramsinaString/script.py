# Find All Anagrams in a String -> Python3

'''
Explanation: Build a hashmap then run a sliding window and when character gets out of it we 
increment the counter and when character gets in we decrement the counter. When all counters in a 
hashmap are 0 we have encountered a anagram. First we initialise the data structure and variables 
then generate a hashmap after which we run a sliding window and perform operations.
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm, res, pl, sl = defaultdict(int), [], len(p), len(s)
        if pl > sl: return []
        for i in p: hm[i] += 1
        for i in range(pl-1): 
            if s[i] in hm: hm[s[i]] -= 1
        for i in range(-1, sl-pl+1):
            if i > -1 and s[i] in hm: hm[s[i]] += 1
            if i+pl < sl and s[i+pl] in hm: hm[s[i+pl]] -=1
            if all(v == 0 for v in hm.values()): res.append(i+1)
        return res