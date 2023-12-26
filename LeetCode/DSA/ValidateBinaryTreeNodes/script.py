# Validate Binary Tree Nodes -> Python3

'''
Explanation: Assume root node is 0 then create set childNodes as sum of left and right child and 
loop on rance n to check if x not in childnodes and set root as x. Maintain seen as set and q as 
deque of array root then loop q and set nod as q popleft. Check if nod in seen to return false then 
add nod in seen and check if leftchild at nod is not same as -1 to append it in q and same for 
rightchild finally return len seen is same as n.
'''

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root, childNodes = 0, set(leftChild + rightChild)
        for x in range(n):
            if x not in childNodes: root = x
        seen, q = set(), deque([root])
        while q:
            nod = q.popleft()
            if nod in seen: return False
            seen.add(nod)
            if leftChild[nod] != -1: q.append(leftChild[nod])
            if rightChild[nod] != -1: q.append(rightChild[nod])
        return len(seen) == n