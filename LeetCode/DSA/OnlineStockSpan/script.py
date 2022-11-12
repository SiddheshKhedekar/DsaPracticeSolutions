# Online Stock Span -> Python3

'''
Explanation: Use stack in init. In next set the res based on last stack insert and its price less 
than current price then increment res by the last res and then append current price and res combo 
to stack and finally return res.
'''

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price: res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res