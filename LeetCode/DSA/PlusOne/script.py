# Plus One -> Python3

'''
Explanation: Set a temp variable to 0, iterate over range of Len array and in Loop increment temp 
by value at i place * pow(10, Len array -1 -i). Return array of int i from looping string num+1.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)): num += digits[i] * pow(10, len(digits)-1-i)
        return [int(i) for i in str(num+1)]