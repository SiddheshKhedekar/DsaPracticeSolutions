# Binary Search Tree Iterator -> Python3

'''
Explanation: Inside init set stk as list and call pushall using root. In pushall while node is not 
none append node in stk and set node as its left. In hasnext return stk and in next set temp as stk 
pop then call pushall with temp right finally return temp val.
'''

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stk = list()
        self.pushAll(root)
    def next(self) -> int:
        temp = self.stk.pop()
        self.pushAll(temp.right)
        return temp.val
    def hasNext(self) -> bool:
        return self.stk
    def pushAll(self, node):
        while node is not None:
            self.stk.append(node)
            node = node.left