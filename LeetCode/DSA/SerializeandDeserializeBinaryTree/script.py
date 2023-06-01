# Serialize and Deserialize Binary Tree -> Python3

'''
Explanation: In serialize initialize valus as array and call doit with root as input then return 
valus as joined string. Inside serialize define doit function and check if node to append str node 
val in valus and call doit recursively for right and left else append # in valus. In deserialize 
set valus as iter of data after split and return doit. In deserialize define doit function and set 
valu as next in valus then check if valus is # and return none. Set node as treenode int valu and 
call doit for left and right and return node.
'''

class Codec:
    def serialize(self, root):
        def doit(node):
            if node:
                valus.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else: valus.append('#')
        valus = []
        doit(root)
        return ' '.join(valus)
    def deserialize(self, data):
        def doit():
            valu = next(valus)
            if valu == '#': return None
            node = TreeNode(int(valu))
            node.left = doit()
            node.right = doit()
            return node
        valus = iter(data.split())
        return doit()