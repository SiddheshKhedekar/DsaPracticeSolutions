# Total Cost to Hire K Workers -> Python3

'''
Explanation: The intuition is to maintain two priority queues pq1 and pq2 that store the candidates 
smallest costs from the beginning and end of the list. In each iteration, the code compares the 
smallest costs from pq1 and pq2 and selects the one with the lowest value. The corresponding cost 
is added to the total cost res, and the element is removed from the respective priority queue. This 
process continues for k iterations, and at the end, the accumulated res value represents the 
minimum total cost required to hire k workers.
'''

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        x, y, pq1, pq2, res = 0, len(costs) - 1, [], [], 0
        while k > 0:
            while len(pq1) < candidates and x <= y:
                heapq.heappush(pq1, costs[x])
                x += 1
            while len(pq2) < candidates and x <= y:
                heapq.heappush(pq2, costs[y])
                y -= 1
            t1 = pq1[0] if pq1 else float('inf')
            t2 = pq2[0] if pq2 else float('inf')
            if t1 <= t2:
                res += t1
                heapq.heappop(pq1)
            else:
                res += t2
                heapq.heappop(pq2)
            k -= 1
        return res