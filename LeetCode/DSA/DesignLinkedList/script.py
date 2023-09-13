# Design Linked List -> Python3

'''
Explanation: Use node class where init initializes val and next to none. In main class initialize 
head and size to 0. Inside addathead call addatindex where index is 0 and in addattail call 
addatindex where index is size. In get check if index < 0 or index >= size and return -1 and same 
if head is none, set curr to head and in for loop in range index set curr to curr.next and return 
curr.val. In the addatindex check if index < 0 or > size return, set node to Node(val) and check if 
index = 0 and set node.next to head and head to node, else set curr to head and check if curr is 
none leading to set head to none else in for loop till index-1 set curr to curr.next out of loop 
set node.next to curr.next and curr.next to node, inc size by 1. In deleteatindex check same as 
first if condition above, set curr to head and if index = 0 set head to curr.next in else run for 
loop till index-1 and set curr to curr.nextout of loop set curr.next to curr.next.next and 
decrement size by 1.

'''

class Node:
    def __init__(self, val): self.val, self.next = val, None
        
class MyLinkedList:
    def __init__(self): self.head, self.size = 0, 0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size: return -1
        if self.head is None: return -1
        curr = self.head
        for i in range(index): curr = curr.next
        return curr.val
    def addAtHead(self, val: int) -> None: self.addAtIndex(0,val)
    def addAtTail(self, val: int) -> None: self.addAtIndex(self.size,val)
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size: return
        node = Node(val)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            if curr is None: self.head = node
            else:
                for i in range(index-1): curr = curr.next
                node.next = curr.next
                curr.next = node
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: return
        curr = self.head
        if index == 0: self.head = curr.next
        else:
            for i in range(index-1): curr = curr.next
            curr.next = curr.next.next
        self.size-=1