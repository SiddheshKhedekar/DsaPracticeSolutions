# Roman to Integer -> Python3

'''
Explanation: Run loop in reverse order. Have a dictionary of values. If first operation using count 
assign value. Else have a temp value for comparison from the previous value and if less then add to 
val else subtract. Assign temp to the current map value at end.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        val, count, temp = 0, 0, 0
        mapVal = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)-1,-1,-1):
            count+=1
            if count == 1: val = mapVal[s[i]]
            else:
                if temp > mapVal[s[i]]: val -= mapVal[s[i]]
                else: val += mapVal[s[i]]
            temp = mapVal[s[i]]
        return val