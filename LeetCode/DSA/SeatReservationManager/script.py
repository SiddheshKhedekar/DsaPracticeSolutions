# Seat Reservation Manager -> Python3

'''
Explanation: In init define heap as list of items in range 1 to n + 1. In reserve return the 
heappop on heap and in unreserve heappush the seatnumber in heap.
'''

class SeatManager:
    def __init__(self, n: int): self.heap = list(range(1, n + 1))
    def reserve(self) -> int: return heapq.heappop(self.heap)
    def unreserve(self, seatNumber: int) -> None: heapq.heappush(self.heap, seatNumber)