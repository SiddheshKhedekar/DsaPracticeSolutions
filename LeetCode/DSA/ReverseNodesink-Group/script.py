# Reverse Nodes in k-Group -> Python3

'''
Explanation: Use temp head and left, right as reversing range. Then use pre and cur to reverse in 
range and skip to connect the reversed ranges.
'''

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = skip = ListNode(0)
        temp.next = left = right = head
        while True:
            cnt = 0
            while right and cnt < k:
                right = right.next
                cnt += 1
            if cnt == k:
                pre, cur = right, left
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                skip.next, skip, left = pre, left, right
            else: return temp.next