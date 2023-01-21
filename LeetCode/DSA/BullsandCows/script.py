# Bulls and Cows -> Python3

'''
Explanation: Bull is count when index and digit guessed correctly and cow is count when digit 
correct but index wrong. First get frequency, then loop both words and get A by traversal and B is 
sum of logical & of frequency values minus A.
'''

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret,guess))
        return '%sA%sB' % (a,sum((s & g).values())-a)