# Course Schedule II -> Python3

'''
Explanation: In main function set graph, ans as defaultdict of list, empty array then looping over 
prerequisites append preq 1 at prereq 0 in graph, also set seen as array of 0 of len numCourses. 
Then loop on range numCourse to check if not dfs i and return empty array otherwise return ans. 
Inside dfs check if seen at nod is -1 to return False then check if it is 1 to return True then set 
seen at nod as -1. Run loop for x in graph at node to check if not dfs at x and return False. Then 
set seen at nod at 1 and append nod in ans and return true.
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.grph, self.ans = collections.defaultdict(list), []
        for prereq in prerequisites: self.grph[prereq[0]].append(prereq[1])
        self.seen = [0 for _ in range(numCourses)]
        def dfs(nod):
            if self.seen[nod] == -1: return False
            if self.seen[nod] == 1: return True
            self.seen[nod] = -1
            for x in self.grph[nod]:
                if not dfs(x): return False
            self.seen[nod] = 1
            self.ans.append(nod)
            return True
        for i in range(numCourses):
            if not dfs(i): return []
        return self.ans