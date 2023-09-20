# Binary Tree Zigzag Level Order Traversal -> Python3

'''
Explanation: Set queue with deque of root, res to [] and direction to 1. Run a loop while queue and 
set level to empty array. Run a for loop of length of queue, pop queue in node and append node 
value in level. If children exist then append then to queue first left then right. Back in while 
loop append the level based on direction to res and update direction.
'''

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque([root])
        result, direction = [], 1
        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            result.append(level[::direction])
            direction *= -1
        return result