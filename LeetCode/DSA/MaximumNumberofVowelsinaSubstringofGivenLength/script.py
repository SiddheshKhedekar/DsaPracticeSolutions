# Maximum Number of Vowels in a Substring of Given Length -> Python3

'''
Explanation: Set temp as list of s, vow as list of vowels and count as 0. Run for loop on range k 
and check if temp at x in vow to increment count by 1. Then set maxN the value of count and run 
another for loop on range k to len s set start as the end - k + 1. Check if temp at start - 1 in 
vow and decrement count also check if temp at end in vow and increment count. Set maxN as the max 
of it and count. Basically maintain a sliding window and maintain count.
'''

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        temp, vow, count = list(s), ['a', 'e', 'i', 'o', 'u'], 0
        for x in range(k):
            if temp[x] in vow: count += 1
        maxN = count
        for end in range(k, len(s)):
            start = end - k + 1
            if temp[start-1] in vow: count -= 1
            if temp[end] in vow: count += 1
            maxN = max(maxN, count)
        return maxN