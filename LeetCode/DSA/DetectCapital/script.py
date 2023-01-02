# Detect Capital -> Python3

'''
Explanation: Check if word is in uppercase or lowercase or titlecase.
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()