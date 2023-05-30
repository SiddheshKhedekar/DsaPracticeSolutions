# Design Parking System -> Python3

'''
Explanation: Define arr in init with array of big, medium, small and in addcar decrement arr at 
cartype - 1 by 1 and return if the arr at same index is greater than ar same as 0.
'''

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.arr = [big, medium, small]
    def addCar(self, carType: int) -> bool:
        self.arr[carType - 1] -= 1
        return self.arr[carType - 1] >= 0