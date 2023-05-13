# Min Stack -> Python3

'''
Explanation: Inside init define que as array. In getmin check if len of que is 0 then return none 
else return the que item at len of que -1,1. In top the same first condition applies and in else 
just return que at len of que -1,0. In pop just pop the que and in push set curmin by calling 
getmin then check if curmin none or val less than curmin to set curmin. At last append val, curmin 
to que.
'''

class MinStack:
    def __init__(self):
        self.que = []
    def push(self, val: int) -> None:
        curMin = self.getMin()
        if curMin == None or val < curMin: curMin = val
        self.que.append((val, curMin))
    def pop(self) -> None:
        self.que.pop()
    def top(self) -> int:
        if len(self.que) == 0: return None
        else: return self.que[len(self.que) - 1][0]
    def getMin(self) -> int:
        if len(self.que) == 0: return None
        else: return self.que[len(self.que) - 1][1]