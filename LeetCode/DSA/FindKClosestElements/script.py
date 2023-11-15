# Find K Closest Elements -> Python3

'''
Explanation: Use window method. Set left and right to 0 and len(arr) - k. Run loop till left is l
ess than right and inside set mid to (left + right ) floor divide by 2. Check if 
x - arr[mid] > arr[mid+k] - x and set left to mid +1 else set right to mid. Return outside loop the 
arr[left:left+k].
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid+k] - x: left = mid + 1
            else: right = mid
        return arr[left:left+k]