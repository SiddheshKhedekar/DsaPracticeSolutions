# Populating Next Right Pointers in Each Node -> Python3

'''
Explanation: Set head to root and loop while root: set cur to root and root to its left. Then run 
loop while cur and inside after checking cur.left set cur.left.next to cur.right. If cur.next set 
cur.right.next to cur.next.left. In else of top if break and then in inside while set cur to 
cur.next. Finally out return head.
'''

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        head = root
        while root:
            cur, root = root, root.left
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                    if cur.next: cur.right.next = cur.next.left
                else: break
                cur = cur.next
        return head