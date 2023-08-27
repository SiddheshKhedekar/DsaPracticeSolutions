# Interleaving String -> Python3

'''
Explanation: Set row, col, ln as len of s1, s2, s3 then check if row + col is not same as ln to 
return false and set stack, visited as array of tuple 0,0 and set of tuple 0,0. Loop while stack to 
set i, j as pop on stack then check if i + j is ln to return true. Also chek if i + 1 is less than 
row and s1 at i is s3 at i + j and tuple of i + 1, j is not in visited. Inside check add i + 1, j 
in stack and also in visited and add similarly for j + 1, s2 finally returning false at loop end.
'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        row, col, ln = len(s1), len(s2), len(s3)
        if row + col != ln: return False
        stack, visited = [(0, 0)], set((0, 0))
        while stack:
            i, j = stack.pop()
            if i + j == ln: return True
            if i + 1 <= row and s1[i] == s3[i + j] and (i + 1, j) not in visited:
                stack.append((i + 1, j))
                visited.add((i + 1, j))
            if j + 1 <= col and s2[j] == s3[i + j] and (i, j + 1) not in visited:
                stack.append((i, j + 1))
                visited.add((i, j + 1))
        return False