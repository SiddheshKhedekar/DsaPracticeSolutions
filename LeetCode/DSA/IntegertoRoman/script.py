# Integer to Roman -> Python3

'''
Explanation: In the dictionary save all values in desc order, iterate on dict and concatenate to 
res the (num//dictval at i) * i and set num to num % dict val at i. Finally, return res.
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        mapVal = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,
                  'V':5,'IV':4,'I':1}
        res = ''
        for i in mapVal:
            res += (num//mapVal[i]) * i
            num %= mapVal[i]
        return res