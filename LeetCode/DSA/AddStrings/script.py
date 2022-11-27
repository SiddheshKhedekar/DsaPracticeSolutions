# Add Strings -> Python3

'''
Explanation: Define temp function where map of number to letter counterpart is initialized. Convert 
both numbers to int using this function and return the sum cast as string.
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(num):
            numdict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
            output = 0
            for i in num: 
                output = output * 10 + numdict[i]
            return output
        return str(str2int(num1)+str2int(num2))