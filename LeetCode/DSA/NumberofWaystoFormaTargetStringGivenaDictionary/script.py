# Number of Ways to Form a Target String Given a Dictionary -> Python3

'''
Explanation: Initialise l as len of target and modulo as given then set ans as sum of array item 
with value 1 with array of 0 of len l. Run for loop on len of first item in words and set counter 
of word index x for each word in words. Then run another for loop in reverse direction on len of 
target and set ans y+1 as increment of ans y after multiplying with count of target y and applying 
modulo. Return last item in ans after modulo.
'''

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        l, modulo = len(target), 10**9 + 7
        ans = [1] + [0] * l
        for x in range(len(words[0])):
            cnt = Counter(w[x] for w in words)
            for y in range(l - 1, -1, -1):
                ans[y + 1] += ans[y] * cnt[target[y]] % modulo
        return ans[l] % modulo