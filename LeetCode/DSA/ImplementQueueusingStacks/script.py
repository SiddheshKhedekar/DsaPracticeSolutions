# Implement Queue using Stacks -> Python3

'''
Explanation: In init define inarr and outarr as empty arrays. In push append x in inarr then in pop 
call peek before returning outarr pop and in empty return not inarr and not outarr. In peek check 
if not out arr then run loop while inarr to append inarr pop in outarr finally return outarr last 
index.
'''

class MyQueue:
    def __init__(self):
        self.in_arr, self.out_arr = [], []
    def push(self, x: int) -> None:
        self.in_arr.append(x)
    def pop(self) -> int:
        self.peek()
        return self.out_arr.pop()
    def peek(self) -> int:
        if not self.out_arr:
            while self.in_arr:
                self.out_arr.append(self.in_arr.pop())
        return self.out_arr[-1]
    def empty(self) -> bool:
        return not self.in_arr and not self.out_arr