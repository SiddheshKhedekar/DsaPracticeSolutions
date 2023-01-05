# Interval List Intersections -> Python3

'''
Explanation: Use two pointers for the lists and run a while loop on both lists. Get the starts and 
ends in variables and check to append to result the max start and min end. Then check which end is 
greater and increment the corresponding pointer.
'''

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j, result = 0, 0, []
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            if a_start <= b_end and b_start <= a_end:
                result.append([max(a_start, b_start), min(a_end, b_end)])
            if a_end <= b_end: i+=1
            else: j+=1
        return result