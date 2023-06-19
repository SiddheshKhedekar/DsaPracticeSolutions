# Pascal's Triangle -> Python3

'''
Explanation: Run loop for num rows. Inside run loop for current loop counter+1. Check if edge and 
add 1 else add the sum of the previous rows j-1 and jth value in temp array. Out of nested loop add 
temp to res.
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i: temp.append(1)
                else: temp.append(res[i-1][j-1]+res[i-1][j])
            res.append(temp)
        return res