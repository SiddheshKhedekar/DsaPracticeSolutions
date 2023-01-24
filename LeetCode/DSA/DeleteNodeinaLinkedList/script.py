# Delete Node in a Linked List -> Python3

'''
Explanation: Set node val to node next val and node next to node second next.
'''

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next