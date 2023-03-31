# Longest Substring Without Repeating Characters -> Python3

'''
Explanation: Set ans, i to 0 and n to len nums also mp to dictionary. For range n run loop on j and 
check if s at j in mp to set i to max of mp[s at j], i. Set ans to max ans and j-i+1 and mp[s at j] 
to j plus 1 finally return ans.
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, i, n, mp = 0, 0, len(s), {}
        for j in range(n):
            if s[j] in mp: i = max(mp[s[j]], i)
            ans = max(ans, j-i+1)
            mp[s[j]] = j+1
        return ans