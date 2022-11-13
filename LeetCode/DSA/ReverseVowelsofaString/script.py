# Reverse Vowels of a String -> Python3

'''
Explanation: Convert string to list, define set of vowels and l r index. Then run while loop l <= r. 
Use the two pointers and swap values using loop and check in set, change pointers accordingly. 
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        s, vows, l, r = list(s), set('aeiouAEIOU'), 0, len(s)-1
        while l <= r:
            while l <= r and s[l] not in vows: l+=1
            while l <= r and s[r] not in vows: r-=1
            if l > r: break
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        return ''.join(s)