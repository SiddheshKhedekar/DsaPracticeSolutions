# Reverse Words in a String III -> Python3

'''
Explanation: Split the string. Reverse the order of words to descending. Join the split array in 
reverse order.
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])[::-1]