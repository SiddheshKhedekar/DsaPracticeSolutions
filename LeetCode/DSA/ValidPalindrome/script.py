# Valid Palindrome -> Python3

'''
Explanation: Set start and end then loop while start less than end to loop again twice and check if 
alphanumeric character encountered and update pointers then check if character lower are not same 
and return false otherwise update pointers again and at end of loop return true.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum(): start += 1
            while start < end and not s[end].isalnum(): end -= 1
            if s[start].lower() != s[end].lower(): return False
            start, end = start + 1, end - 1
        return True