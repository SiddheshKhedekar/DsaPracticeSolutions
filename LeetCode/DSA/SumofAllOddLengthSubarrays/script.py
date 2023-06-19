# Sum of All Odd Length Subarrays -> Python3

'''
Explanation: Use brute force method with two loops nested such that upper i runs for length of arr 
as l. Inner loop runs for i to l in hops of 2. Inside get the sum of array contents from i to j+1.
'''

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        summ, l = 0, len(arr)
        for i in range(l):
            for j in range(i,l,2): summ += sum(arr[i:j+1])
        return summ