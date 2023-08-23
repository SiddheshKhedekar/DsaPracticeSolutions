# Excel Sheet Column Title -> Python3

'''
Explanation: Set res as empty array and run loop while colNo is greater than 0. Inside decrement 
colNo by 1 and set crnt as mod of colNo by 26 then set colNo as floor division by 26 then append 
chr of crnt + ord A in res and finally out of loop return the joined form of res in reverse.
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            columnNumber -= 1
            crnt = columnNumber % 26
            columnNumber = int(columnNumber // 26)
            res.append(chr(crnt + ord('A')))
        return ''.join(res[::-1])