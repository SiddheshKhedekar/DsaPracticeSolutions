# Spiral Matrix II -> Python3

'''
Explanation: Set the empty array and low to n*n+1 while the low is greater than 1 decrement low by 
the length of the array and set high to low. Set the array to the range of low to high and the 
rotation on the array.
'''

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans, low = [], n * n + 1
        while low > 1:
            low, high = low - len(ans), low
            ans = [range(low, high)] + list(zip(*ans[::-1]))
        return ans