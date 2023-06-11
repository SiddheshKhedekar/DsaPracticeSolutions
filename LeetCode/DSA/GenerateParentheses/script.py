# Generate Parentheses -> Python3

'''
Explanation: Set ans as empty array and call dfs with 0, 0, ''. Inside dfs check if len string is 
n * 2 and append string in ans then return. Check if lft is less than n and call dfs with left+1, 
right, string plus open bracket. Check if right is less than left and call dfs with left, right+1, 
string + closed bracket.
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(lft, rght, strng):
            if len(strng) == n * 2:
                ans.append(strng)
                return
            if lft < n: dfs(lft + 1, rght, strng + '(')
            if rght < lft: dfs(lft, rght + 1, strng + ')')
        ans = []
        dfs(0, 0, '')
        return ans