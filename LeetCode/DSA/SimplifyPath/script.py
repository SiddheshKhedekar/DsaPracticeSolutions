# Simplify Path -> Python3

'''
Explanation: Initialize stack and loop on path split using / and if stack exists and current 
element is .. then pop stack else if element not blank . or .. append element in stack then finally 
join and return.
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        for elm in path.split('/'):
            if stk and elm == '..': stk.pop()
            elif elm not in ['.', '', '..']: stk.append(elm)
        return '/' + '/'.join(stk)