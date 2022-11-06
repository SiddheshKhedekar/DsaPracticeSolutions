# Duplicate Zeros -> Python3

'''
Explanation: Insert at index where value 0. Check count of insert and del last item.
'''

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = len(arr)
        i = 0
        while i<count:
            if arr[i] == 0:
                arr.insert(i,0)
                i+=1
            i+=1
        for i in range(len(arr)-1,count-1,-1):    
            del arr[i]