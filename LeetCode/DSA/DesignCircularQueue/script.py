# Design Circular Queue -> Python3

'''
Explanation: Use listnode class with default val and next and in main class initialize maxsize to 
k, size to 0 and head tail to none. In the isfull return size is maxsize. In the osempty return is 
size 0. In the rear check if isempty and return -1 else return tail.val, similarly in front return 
head.val. In the dequeue check same base condition and after that set head to head.next and 
decrement size by one, return true. In the enqueue function check iffull and return false define a 
listnode object and if isempty set head and tail to newnode. Else set tail.nxt to newnode and tail 
to tail.nxt. Increment size by 1 and return true.

'''

class ListNode:
    def __init__(self, val, nxt = None): self.val, self.nxt = val, nxt

class MyCircularQueue:
    def __init__(self, k: int): self.maxSize, self.size, self.head, self.tail = k, 0, None, None
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False 
        newNode = ListNode(value)
        if self.isEmpty(): self.head = self.tail = newNode 
        else:
            self.tail.nxt = newNode 
            self.tail = self.tail.nxt
        self.size+=1
        return True
    def deQueue(self) -> bool:
        if self.isEmpty(): return False 
        self.head = self.head.nxt
        self.size-=1
        return True
    def Front(self) -> int: return -1 if self.isEmpty() else self.head.val
    def Rear(self) -> int: return -1 if self.isEmpty() else self.tail.val
    def isEmpty(self) -> bool: return self.size == 0
    def isFull(self) -> bool: return self.size == self.maxSize