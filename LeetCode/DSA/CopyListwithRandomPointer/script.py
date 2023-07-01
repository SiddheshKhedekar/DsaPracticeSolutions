# Copy List with Random Pointer -> Python3

'''
Explanation: Set dct as defaultdict of lambda call to Node and set dct none to none and nod to head 
then run loop while nod. Inside set dct at node val as nod val, dct at nod next as dct node.next, 
dct at nod random as dct nod.random and nod as its next. Finally return the dct at head.
'''

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dct = defaultdict(lambda: Node(0))
        dct[None], nod  = None, head
        while nod:
            dct[nod].val = nod.val
            dct[nod].next = dct[nod.next]
            dct[nod].random = dct[nod.random]
            nod = nod.next
        return dct[head]