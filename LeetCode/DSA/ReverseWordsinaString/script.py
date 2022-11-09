# Reverse Words in a String -> Python3

'''
Explanation: Split the string reverse it as array and return the string after joining it back.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))