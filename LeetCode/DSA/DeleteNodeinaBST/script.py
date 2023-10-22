# Delete Node in a BST -> Python3

'''
Explanation: Check root not valid and return none. Check if root val is key else if it is greater 
than key and call recursive for root left and key and save in root left else do similar for right. 
If value match key then check if right exist else return left and viceversa then if root and left 
both exist set dummy as root right and while dummy has left set temp left to temp. On loop end set 
root val as temp val and set root right to the recursive call of root right and root val.
'''

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None
        if root.val == key:
            if not root.right: return root.left
            if not root.left: return root.right
            if root.right and root.left:
                dummy = root.right
                while dummy.left: dummy = dummy.left
                root.val = dummy.val
                root.right = self.deleteNode(root.right, root.val)
        elif root.val > key: root.left = self.deleteNode(root.left, key)
        else: root.right = self.deleteNode(root.right, key)
        return root