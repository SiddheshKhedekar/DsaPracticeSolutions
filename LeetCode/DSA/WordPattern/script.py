# Word Pattern -> Python3

'''
Explanation: Split the string as words in array and check if length of pattern matches the array 
and also check if the length of the set of pattern and set of array and set of zipped pattern and 
array is the same.
'''

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        return len(pattern) == len(t) and \
        len(set(pattern)) == len(set(t)) == len(set(zip(pattern,t)))