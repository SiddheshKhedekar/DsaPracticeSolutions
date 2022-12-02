# Determine if Two Strings Are Close -> Python3

'''
Explanation: Check if the set of the words are equal and frequencies are the same.
'''

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and \
        Counter(Counter(word1).values()) == Counter(Counter(word2).values())