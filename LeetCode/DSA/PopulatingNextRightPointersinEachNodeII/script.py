# Populating Next Right Pointers in Each Node II -> Python3

'''
Explanation: We need to traverse each tree level and check the .next conditions. Loop of n after 
initializing it with root and set two empty trees inside. Run another loop on n and if left or 
right of n exist then set current.next and current. Set n to its next before first loop end and 
after set n to next of temp.
'''

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        n = root
        while n:
            current = temp = Node(0)
            while n:
                if n.left:
                    current.next = n.left
                    current = current.next
                if n.right:
                    current.next = n.right
                    current = current.next
                n = n.next
            n = temp.next
        return root