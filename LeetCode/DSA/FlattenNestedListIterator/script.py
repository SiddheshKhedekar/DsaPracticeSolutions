# Flatten Nested List Iterator -> Python3

'''
Explanation: In init define stk as the array with array item nestedlist, 0 then in next check if 
next exists and set nstdlist, n as the last item in stk,increment count at last item in stack by 1 
and return the nstdlist value at n as getinteger. In hasnext assign stk to s and run loop while s 
assign nstdlist and n as s at last index and check if n is same as len od nstdlist to pop s else 
set a as nstdlist at n check if a value is integer to return true then increment count at last item 
in s and append a as getlist with 0 in s finally return false outside loop.
'''

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]): self.stk = [[nestedList, 0]]
    def next(self) -> int:
        self.hasNext()
        nstdList, n = self.stk[-1]
        self.stk[-1][1] += 1
        return nstdList[n].getInteger()
    def hasNext(self) -> bool:
        s = self.stk
        while s:
            nstdList, n = s[-1]
            if n == len(nstdList): s.pop()
            else:
                a = nstdList[n]
                if a.isInteger(): return True
                s[-1][1] += 1
                s.append([a.getList(), 0])
        return False