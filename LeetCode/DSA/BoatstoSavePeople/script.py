# Boats to Save People -> Python3

'''
Explanation: Sort the people and initialize low high and count. Run while loop till low is less 
than high and check if value at low plus value at high is less than or same as limit and update 
indexes by 1 else only update high. Before loop rerun increment count.
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, h, count = 0, len(people) - 1, 0
        while l <= h:
            if people[l] + people[h] <= limit:
                l += 1
                h -= 1
            else: h -= 1
            count += 1
        return count