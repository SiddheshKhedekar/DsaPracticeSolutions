# Letter Combinations of a Phone Number -> Python3

'''
Explanation: Set ans as empty array and dct as the dict of number and alphabet map. Check if len 
digits is 0 to return ans then call dfs with digits, 0, dct, ‘’, ans. Inside dfs check if index is 
greater than len digits to append path in ans and return. Set tempStr as dct at digits at index 
then run loop for x in tempStr and inside call dfs with digits, index+1, dct, path+x, ans.
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(digits, indx, dct, path, ans):
            if indx >= len(digits):
                ans.append(path)
                return
            tempStr = dct[digits[indx]]
            for x in tempStr:
                dfs(digits, indx + 1, dct, path + x, ans)
        ans, dct = [], {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', \
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0: return ans
        dfs(digits, 0, dct, '', ans)
        return ans