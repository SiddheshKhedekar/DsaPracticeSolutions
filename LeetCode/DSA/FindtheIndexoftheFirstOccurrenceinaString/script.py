# Find the Index of the First Occurrence in a String -> Python3

'''
Explanation: Split the string as words in array and check if length of pattern matches the array 
and also check if the length of the set of pattern and set of array and set of zipped pattern and 
array is the same.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0] and needle == haystack[i:i+len(needle)]: return i
        return -1