# Palindrome Partitioning -> Python3

'''
Explanation: Define a function to check string is palindrome and another to dfs on string with path 
and result string parameters. In dfs function append to result when string empty and loop on string 
length checking if palindrome to x and call dfs with string after x and path + string till x.
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPalindrome(string): return string == string[::-1]
        def dfs(string, p, ans):
            if not string:
                ans.append(p)
                return
            for x in range(1, len(string) + 1):
                if isPalindrome(string[:x]):
                    dfs(string[x:], p+[string[:x]], ans)
        dfs(s, [], ans)
        return ans