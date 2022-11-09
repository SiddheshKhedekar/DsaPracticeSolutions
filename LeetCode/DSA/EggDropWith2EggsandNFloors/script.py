# Egg Drop With 2 Eggs and N Floors -> Python3

'''
Explanation: We have 2 eggs, after losing first we reduce the remaining floors to i. Then we first 
check for i-1 and if egg did not break we check for n-i floors reqursively.
'''

class Solution:
    @cache
    def twoEggDrop(self, n: int) -> int:
        return min((1 + max(i-1,self.twoEggDrop(n-i)) for i in range(1, n)) ,default = 1)