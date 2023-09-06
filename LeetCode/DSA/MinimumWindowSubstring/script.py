# Minimum Window Substring -> Python3

'''
Explanation: Set need to counter t and missing to len t also define i I and J to 0. Run for loop 
where j,c enumerate on s,1 inside set decrement missing by need[c] > 0 and then decrement need[c] 
by 1 check if not missing and run while loop inside for i<j and need[s[i]] <0. Inside increment 
need[s[i]] by 1 and same for i. Check if not J or j -i <= J-I and set i,j to i, j finally return 
s[I,J] outside loops.
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I: I, J = i, j
        return s[I:J]