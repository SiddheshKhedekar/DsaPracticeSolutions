# Minimum Time to Make Rope Colorful -> Python3

'''
Explanation: Set i,j,total to 0. While i < len needed time and j < len of needed time run loop. Set 
the cur total to curmax to 0. While j is less than len needed time and colors i == colors j. 
Increment the cur total by needed time j in curmax get hte max of curr_max and neededtime j and 
increment j. Outside inner while Increment total time by the curtotal - currmax and set i = j. 
Outside loop return total time 
'''

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = j = total_time = 0
        while i < len(neededTime) and j < len(neededTime):
            curr_total = curr_max = 0
            while j < len(neededTime) and colors[i] == colors[j]:
                curr_total += neededTime[j]
                curr_max = max(curr_max, neededTime[j])
                j+=1
            total_time += curr_total - curr_max
            i = j
        return total_time