# Water and Jug Problem -> Python3

'''
Explanation: Return if target capacity is 0 or if the sum of jugs is greater than or same as target 
and target mod by the gcd of jugs is 0.
'''

class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        return targetCapacity == 0 or jug1Capacity + jug2Capacity >= targetCapacity and \
            targetCapacity % gcd(jug1Capacity, jug2Capacity) == 0