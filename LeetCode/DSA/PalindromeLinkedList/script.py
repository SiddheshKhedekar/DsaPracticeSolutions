# Palindrome Linked List -> Python3

'''
Explanation: Set rev, fast to none and head. In while fast and fast.next set fast, rev, rev.next 
and head to fast.next.next, head rev and head.next. Set tail to head.next if fast else head. Set 
ispali to true first and then run while loop till rev and inside set ispali to ispali and 
rev val == tail val then set head, head.next, rev, tail to rev, head, rev.next, tail.next and 
return ispali. The second while helps set the original list correct.
'''

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev, fast = None, head
        while fast and fast.next: fast, rev, rev.next, head = fast.next.next, head, rev, head.next
        tail = head.next if fast else head
        isPali = True
        while rev:
            isPali = isPali and rev.val == tail.val
            head, head.next, rev, tail = rev, head, rev.next, tail.next
        return isPali