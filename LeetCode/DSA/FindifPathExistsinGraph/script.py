# Find if Path Exists in Graph -> Python3

'''
Explanation: Add neighbours in a defaultdict then set deque and seen. run while loop of queue and 
if node is destination then true else check by looping all neighbours of node. Add to seen and 
queue if not already in seen.
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        neighbors = defaultdict(list)
        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)
        q, seen = deque([source]), set([source])
        while q:
            node = q.popleft()
            if node == destination: return True
            for n in neighbors[node]:
                if n not in seen:
                    seen.add(n)
                    q.append(n)
        return False