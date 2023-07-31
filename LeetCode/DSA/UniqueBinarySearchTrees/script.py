# Unique Binary Search Trees -> Python3

'''
Explanation: Best approach is to use catalan numbers where for all x in range of n we get the 
product of the values after 4 * x + 2 and dividing by x + 2 and return the value casted as int.
'''

class Solution:
    def numTrees(self, n: int) -> int:
        return int(prod((4 * x + 2) / (x + 2) for x in range(n)))