# Perfect Squares -> Python3

'''
Explanation: Create list of squares and run a while loopon elements tocheck. Increment count and 
create new set iterate x, y on tocheck and list if x is equal to y return count if x < y then break 
else app x-y to temp and out of for loops set tocheck to temp.
'''

class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2: return n
        lst, i, cnt, toCheck = [], 1, 0, {n}
        while i * i <= n:
            lst.append(i*i)
            i+=1
        while toCheck:
            cnt+=1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y: return cnt
                    if x < y: break
                    temp.add(x-y)
            toCheck = temp
        return cnt