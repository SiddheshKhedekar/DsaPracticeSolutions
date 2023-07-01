# Fair Distribution of Cookies -> Python3

'''
Explanation: Backtracking algorithm exhaustively explores all possible combinations of assigning 
cookies to children. It starts with an empty distribution and recursively assigns each cookie to 
one of the children, backtracking when needed to explore other possibilities. The fair variable is 
updated whenever a complete distribution is achieved (all cookies processed). The maximum value in 
the distribution array represents the unfairness of the current distribution. By minimizing this 
maximum unfairness value, the algorithm finds the distribution with the minimum unfairness among 
all possible combinations.
'''

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        res, fair = float('inf'), [0] * k
        def backtrack(x):
            nonlocal res, fair
            if x == len(cookies):
                res = min(res, max(fair))
                return
            if res <= max(fair): return
            for y in range(k):
                fair[y] += cookies[x]
                backtrack(x + 1)
                fair[y] -= cookies[x]
        backtrack(0)
        return res