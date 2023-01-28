# Concatenated Words -> Python3

'''
Explanation: Create a set of words and initialize arroy output. Define a dfs function and loop from 
1 to length of word and set the prefix and suffix. Check for conditions of prefix and suffix in 
wordset and also dfs call for them and return true. In main function loop of words and check call 
to dfs function and append word to ans. 
'''

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet, ans = set(words), []
        def dfs(w):
            for i in range(1, len(w)):
                pre, suf = w[:i], w[i:]
                if pre in wordSet and suf in wordSet: return True
                if pre in wordSet and dfs(suf): return True
                if suf in wordSet and dfs(pre): return True
            return False
        for x in words:
            if dfs(x): ans.append(x)
        return ans