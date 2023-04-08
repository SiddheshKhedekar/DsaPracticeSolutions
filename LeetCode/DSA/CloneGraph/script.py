# Clone Graph -> Python3

'''
Explanation: Check if not node and return it then initialize a queue with deque of array node and 
hashmap of clones with node val key and value Node passing val and new array. Run loop while queue 
and set cur using popleft on queue then set current clone to the value in clones at key cur val. 
Run loop for nbr in cur nbrs, check if val not in clones set clones at nbr val to new node with 
nbr val, empty array and append nbr to queue. Before loop rerun append clones at nbr val to 
cur clone nbrs. Finally return the clones at node val.
'''

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        que, clones = deque([node]), {node.val: Node(node.val, [])}
        while que:
            crnt = que.popleft()
            crnt_clone = clones[crnt.val]
            for nbr in crnt.neighbors:
                if nbr.val not in clones:
                    clones[nbr.val] = Node(nbr.val, [])
                    que.append(nbr)
                crnt_clone.neighbors.append(clones[nbr.val])
        return clones[node.val]