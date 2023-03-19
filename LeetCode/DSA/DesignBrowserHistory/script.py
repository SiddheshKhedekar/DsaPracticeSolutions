# Design Browser History -> Python3

'''
Explanation: At initialization set history as array with homepage and crnt, size to 0. On visit 
increment crnt and check if it is the same as length of hist and append url to hist else set hist 
at crnt to url and update size as crnt. On back set crnt to max of crnt - steps, 0 and on forward 
set it to min of crnt + steps, size. In both return hist value at crnt. 
'''

class BrowserHistory:
    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.crnt = 0
        self.size = 0
    def visit(self, url: str) -> None:
        self.crnt += 1
        if self.crnt == len(self.hist): self.hist.append(url)
        else: self.hist[self.crnt] = url
        self.size = self.crnt
    def back(self, steps: int) -> str:
        self.crnt = max(self.crnt - steps, 0)
        return self.hist[self.crnt]
    def forward(self, steps: int) -> str:
        self.crnt = min(self.crnt + steps, self.size)
        return self.hist[self.crnt]