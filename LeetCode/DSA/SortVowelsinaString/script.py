# Sort Vowels in a String -> Python3

'''
Explanation: Set vwls as the reverse sorted array of all vowels in s. Then loop for c in s and 
check if c is vowel to append vwls pop in res else append c to res. Lastly join str res and return.
'''

class Solution:
    def sortVowels(self, s: str) -> str:
        vwls, res = sorted([x for x in s if x.lower() in 'aeiou'], reverse = True), []
        for c in s:
            if c.lower() in 'aeiou': res.append(vwls.pop())
            else: res.append(c)
        return ''.join(res)