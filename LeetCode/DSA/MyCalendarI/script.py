# My Calendar I -> Python3

'''
Explanation: Define a node class with init params s, e and set self s, e along with right and left 
as none then in calendar class set the self root as none in init. In book function check if not 
root to set root as new node with start and end then return true otherwise return bookhelper with 
start, end, root. Inside bookhelper check if s is greater than or same as node e then check if node 
right to return the bookhelper with node right else set new node as node right returning true. In 
above if check elseif e is less than or same as node s and inside check if node left to return the 
bookhelper with node left else set node left as new node and return true at end in above if else 
return true.
'''

class Node:
    def __init__(self, s, e): self.e, self.s, self.left, self.right = e, s, None, None

class MyCalendar:
    def __init__(self): self.root = None
    def book_helper(self, s, e, node):
        if s >= node.e:
            if node.right: return self.book_helper(s, e, node.right)
            else:
                node.right = Node(s, e)
                return True
        elif e <= node.s:
            if node.left: return self.book_helper(s, e, node.left)
            else:
                node.left = Node(s, e)
                return True
        else: return False
    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.book_helper(start, end, self.root)