# Number of Laser Beams in a Bank -> Python3

'''
Explanation: Set res and pre to 0 then loop for x in bank. Inside set y as cnt of '1' in x and 
check if y to increment res by the multiplication of pre and y then set pre as y. Finally out of 
loop return res.
'''

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = pre = 0
        for x in bank:
            y = x.count('1')
            if y:
                res += pre * y
                pre = y
        return res