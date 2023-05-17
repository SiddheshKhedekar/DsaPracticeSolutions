# Smallest Number in Infinite Set -> Python3

'''
Explanation: On initialize set crnt as 1 and mem as a set. In popsmall check if mem and set ans as 
the min of mem then remove ans from mem and return ans else increment crnt by 1 and return 
crnt - 1. In addback check if crnt greater than num and add num in mem.
'''

class SmallestInfiniteSet:
    def __init__(self):
        self.crnt, self.mem = 1, set()
    def popSmallest(self) -> int:
        if self.mem:
            ans = min(self.mem)
            self.mem.remove(ans)
            return ans
        else:
            self.crnt += 1
            return self.crnt - 1
    def addBack(self, num: int) -> None:
        if self.crnt > num: self.mem.add(num)