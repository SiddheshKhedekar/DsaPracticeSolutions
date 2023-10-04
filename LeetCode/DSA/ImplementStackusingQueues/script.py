# Implement Stack using Queues -> Python3

'''
Explanation: In init set que as deque, in pop return popleft on que, in top return the que at 0 
index and in empty check if not len of que. In push set q as que and append x in q then loop on 
range of len q to append q popleft in q.
'''

class MyStack:
    def __init__(self): self._que = deque()
    def push(self, x: int) -> None:
        q = self._que
        q.append(x)
        for _ in range(len(q) - 1): q.append(q.popleft())
    def pop(self) -> int: return self._que.popleft()
    def top(self) -> int: return self._que[0]
    def empty(self) -> bool: return not len(self._que)