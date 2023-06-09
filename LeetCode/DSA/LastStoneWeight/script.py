# Last Stone Weight -> Python3

'''
Explanation: Set to h the value [-x for x in stones]. Heapq.heapify h and in while len(h) > 1 and 
h[0] != 0 loop do heapq.heappush(h,heapq.heappop(h) - heapq.heappop(h)) and return -h[0].
'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)
        while len(h) > 1 and h[0] != 0:
            heapq.heappush(h,heapq.heappop(h) - heapq.heappop(h))
        return -h[0]