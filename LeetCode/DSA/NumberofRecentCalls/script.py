# Number of Recent Calls -> Python3

'''
Explanation: Inside init we initialise dque as deque and in ping append t to dque then run loop 
while dque at 0 is less than t - 3000 to popleft dque and finally return len dque at end of loop.
'''

class RecentCounter:
    def __init__(self): self.dque = deque()
    def ping(self, t: int) -> int:
        self.dque.append(t)
        while self.dque[0] < t - 3000: self.dque.popleft()
        return len(self.dque)