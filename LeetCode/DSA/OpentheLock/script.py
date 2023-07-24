# Open the Lock -> Python3

'''
Explanation: Implement bfs to generate all possible combo of locks starting with 0000 and for each 
step we generate neighbors of current state by turning all wheels in both directions to check if 
they are deadend. If we meet target in current step is the min num of turns to open lock.
'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(code):
            for z in range(4):
                x = int(code[z])
                for dif in (-1, 1):
                    y = (x + dif + 10) % 10
                    yield code[:z] + str(y) + code[z + 1:]
        deadSet = set(deadends)
        if "0000" in deadSet: return -1
        que, stps = deque(["0000"]), 0
        while que:
            for _ in range(len(que)):
                cur = que.popleft()
                if cur == target: return stps
                for nei in neighbors(cur):
                    if nei in deadSet: continue
                    deadSet.add(nei)
                    que.append(nei)
            stps += 1
        return -1