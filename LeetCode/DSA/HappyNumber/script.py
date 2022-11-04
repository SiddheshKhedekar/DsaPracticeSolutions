# Happy Number -> Python3

'''
Explanation: Set memory to check if the number from the operation is cycling.
'''

class Solution:
    def isHappy(self, n: int) -> bool:
        memory = []
        while n not in memory:
            memory.append(n)
            temp = 0
            for i in str(n):
                temp += (int(i)*int(i))
            n = temp
        return n == 1