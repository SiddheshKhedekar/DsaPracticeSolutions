# Find Smallest Letter Greater Than Target -> Python3

'''
Explanation: If target is greater than the last index value or less than first value then return 
first value. Run loop while start(0) is less than end(len-1) set temp to (end+start)//2. If value 
at temp is less than target them set start to temp+1. If temp value is greater than target set end 
to temp-1 and outside loop return value at start.
'''

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]: return letters[0]
        start = 0
        end = len(letters)-1
        while (start <= end):
            temp = (end+start)//2
            if (letters[temp] <= target): start = temp + 1
            if (letters[temp] > target): end = temp - 1
        return letters[start]