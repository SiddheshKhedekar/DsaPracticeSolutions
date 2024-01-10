# Amount of Time for Binary Tree to Be Infected -> Python3

'''
Explanation: Create a grph as default dict along with stk as list of tuple node, prnt using a while 
loop. Then set res as -1 visited as dict with start and q as deque of start. Loop while q and nest 
loop for len range len q to check if node visited and append to q incrementing loop for each outer 
most loop. Finally return res at end.
'''

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        grph, stk = defaultdict(list), [(root, None)]
        while stk:
            nod, prnt = stk.pop()
            if prnt:
                grph[prnt.val].append(nod.val)
                grph[nod.val].append(prnt.val)
            if nod.left: stk.append((nod.left, nod))
            if nod.right: stk.append((nod.right, nod))
        res, visited, q = -1, {start}, deque([start])
        while q:
            for _ in range(len(q)):
                x = q.popleft()
                for y in grph[x]:
                    if y not in visited:
                        visited.add(y)
                        q.append(y)
            res += 1
        return res