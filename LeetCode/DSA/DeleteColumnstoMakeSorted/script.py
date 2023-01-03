# Delete Columns to Make Sorted -> Python3

'''
Explanation: Get columns as array from input and check them with the sorted columns to get count.
'''

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(list(col) != sorted(col) for col in zip(*strs))