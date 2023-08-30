# Flatten a Multilevel Doubly Linked List -> Python3

'''
Explanation: Use dummy as node 0, set cur to dummy and stack to list head. While stack pop in last 
check its next and child separately and append to stack. Set cur next to last, last prev to cur, 
cur child to none and cur to last. After while set res to dummy next and rest prev to none before 
returning res.
'''

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        dummy = Node(0)
        curr, stack = dummy, [head]
        while stack:
            last = stack.pop()
            if last.next: stack.append(last.next)
            if last.child: stack.append(last.child)
            curr.next = last
            last.prev = curr
            last.child = None
            curr = last
        res = dummy.next
        res.prev = None
        return res