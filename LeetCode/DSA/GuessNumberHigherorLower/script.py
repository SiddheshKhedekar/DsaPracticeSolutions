# Guess Number Higher or Lower -> Python3

'''
Explanation: Set start as 1 and end as n then run loop while start is less than or same as end and 
check if temp that is the mid of start and end is correct by calling guess. If guess returns 
negative then reduce end to temp else if positive update start to temp.
'''

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        while (start <= end):
            temp = start+(end-start)//2
            if (guess(temp) == 0): return temp
            elif (guess(temp) == -1): end = temp-1
            elif (guess(temp) == 1): start = temp+1