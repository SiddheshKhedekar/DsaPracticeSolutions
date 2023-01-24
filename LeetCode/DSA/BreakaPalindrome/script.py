# Break a Palindrome -> Python3

'''
Explanation: Iterate through string and append a at first position not a otherwise append b at end.
'''

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' +  palindrome[i+1:]
        return palindrome[:-1] + 'b' if palindrome[:-1] else ''