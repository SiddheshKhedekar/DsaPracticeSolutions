# Sum of Subarray Minimums -> Python3

'''
Explanation: Add 0 at start of stack to avoid empty array and initialize result, stack as 0 array 
of len arr, 0 as array. Then loop of arr and check while value at last stack in arr is greater than 
arr at i to pop stack. Set ja as last stack item and update result at i and append i in stack. 
Finally return the sum of result after modulo by given value.
'''

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0]+arr
        result, stack = [0]*len(arr), [0]
        for i in range(len(arr)):
            while arr[stack[-1]] > arr[i]: stack.pop()
            j = stack[-1]
            result[i] = result[j] + (i-j)*arr[i]
            stack.append(i)
        return sum(result) % (10**9+7)