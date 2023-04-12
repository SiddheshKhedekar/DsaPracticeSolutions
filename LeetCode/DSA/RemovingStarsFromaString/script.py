# Removing Stars From a String -> Python3

'''
Explanation: Use stack to append while not * else pop from the stack and return the joined stack.
'''

class Solution:
    def removeStars(self, s: str) -> str:
        st = []
        for i in s:
            if i != '*': st.append(i)
            else: st.pop()
        return ''.join(st)