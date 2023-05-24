# Kth Largest Element in a Stream -> Python3

'''
Explanation: In init define self vars pool as nums and k as k then heapify pool. Run loop while 
pool len is greater than k to pop the heap pool. In add check if len less than k to push val in 
pool else if val greater than pool 0 replace val in pool and return pool 0.
'''

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.pool, self.k = nums, k
        heapq.heapify(self.pool)
        while len(self.pool) > k: heapq.heappop(self.pool)
    def add(self, val: int) -> int:
        if len(self.pool) < self.k: heapq.heappush(self.pool, val)
        elif val > self.pool[0]: heapq.heapreplace(self.pool, val)
        return self.pool[0]