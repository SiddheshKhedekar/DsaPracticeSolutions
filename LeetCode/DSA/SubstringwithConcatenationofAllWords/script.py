# Substring with Concatenation of All Words -> Python3

'''
Explanation: Set wl as len of item at 0 in words, wsl as len of words multiplied by wl and ans as 
empty array. Loop for p in range of wl to set x as p and f as the counter of words then loop on y 
in range of x to len s + 1 - wl in steps of wl. Inside set wrd as s from y to y + wl and decrement 
f at wrd by 1. Again loop while f at wrd is less than 0 to increment f as s x to x + wl by 1 and x 
by wl and out of this loop check if x + wsl is same as y + wl to append x in ans then at end of all 
loops return ans.
'''

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wl, wsl, ans = len(words[0]), len(words) * len(words[0]), []
        for p in range(wl):
            x, f = p, Counter(words)
            for y in range(x, len(s) + 1 - wl, wl):
                wrd = s[y: y + wl]
                f[wrd] -= 1
                while f[wrd] < 0:
                    f[s[x: x + wl]] += 1
                    x += wl
                if x + wsl == y + wl: ans.append(x)
        return ans