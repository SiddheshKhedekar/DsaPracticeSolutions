# Maximum Width of Binary Tree -> Python3

'''
Explanation: Initialise lvlOld, numOld, maxWdth as 1, 1, 0 and set que as deque with array of 
arrayitem consisting lvlOld, numOld, root. Then loop while que and popleft on que to get new 
arrayitem of num, lvl, node. Check if lvl is greater than lvlOld and swap lvlOld, lvl along with 
numOld, num. Set maxWdth as max of itself and num - numOld + 1 then check if node left exists and 
append to que the arrayitem with num*2, lvl+1, left node and same for right with its respective 
num*2+1, lvl+1, node right. 
'''

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lvlOld, numOld, maxWdth = 1, 1, 0
        que = deque([[lvlOld, numOld, root]])
        while que:
            [num, lvl, node] = que.popleft()
            if lvl > lvlOld: lvlOld, numOld = lvl, num
            maxWdth = max(maxWdth, num - numOld + 1)
            if node.left: que.append([num*2, lvl+1, node.left])
            if node.right: que.append([num*2+1, lvl+1, node.right])
        return maxWdth