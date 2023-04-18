# Merge Strings Alternately -> Python3

'''
Explanation: Return joined string after adding the characters in strings using loop and zip_longest.
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(x + y for x, y in zip_longest(word1, word2, fillvalue = ''))