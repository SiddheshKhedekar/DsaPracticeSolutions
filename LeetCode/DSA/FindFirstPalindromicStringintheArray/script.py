# Find First Palindromic String in the Array -> Python3

'''
Explanation: Traverse array and for each item check if it is the same as its reverse to return it 
otherwise return empty.
'''

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((wrd for wrd in words if wrd == wrd[::-1]), "")