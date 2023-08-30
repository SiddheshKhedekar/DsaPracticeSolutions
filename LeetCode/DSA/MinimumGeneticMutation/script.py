# Minimum Genetic Mutation -> Python3

'''
Explanation: Use queue with start 0 and set dict seen loop queue for bfs and set node , steps if 
node is end return steps first loop protein digits then Len of sequence create new neighbour and 
then check if in bank before appending to queue and set return -1 at end otherwise.
'''

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        queue, seen = deque([(start,0)]), {start}
        while queue:
            node, steps = queue.popleft()
            if node == end: return steps
            for c in "ACGT":
                for i in range(len(node)):
                    neighbour = node[:i] + c + node[i+1:]
                    if neighbour not in seen and neighbour in bank:
                        queue.append((neighbour,steps+1))
                        seen.add(neighbour)
        return -1