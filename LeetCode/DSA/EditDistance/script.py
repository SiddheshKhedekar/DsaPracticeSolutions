# Edit Distance -> Python3

'''
Explanation: Create a 2d matrix of memory and set the values for index based of the lengths of 
grid. Run a loop on foth lengths nested and check if the chars in words at index are same and set 
mem to the previous indices else set it to 1 + the min of the previous indices including diagonals. 
Finally we have answer in last element of grid.
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        x, y = len(word1), len(word2)
        mem = [[0] * (y + 1) for _ in range(x + 1)]
        for a in range(x + 1): mem[a][0] = a
        for b in range(y + 1): mem[0][b] = b
        for a in range(1, x + 1):
            for b in range(1, y + 1):
                if word1[a - 1] == word2[b - 1]: mem[a][b] = mem[a - 1][b - 1]
                else:
                    mem[a][b] = 1 + min(mem[a - 1][b], mem[a][b - 1], mem[a - 1][b - 1])
        return mem[-1][-1]