# Asteroid Collision -> Python3

'''
Explanation: Initialize ans as empty array and then loop for astroid in asteroids. Then run loop 
while len ans and astroid is less than 0 and ans at last index is greater than 0. Check if last ans 
is -astroid and pop ans and break else if last ans is less than -astroid than pop ans and continue 
else if ans at last index is greater than - astroid then break and in else of while append astroid 
to ans.
'''

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for astroid in asteroids:
            while len(ans) and astroid < 0 and ans[-1] > 0:
                if ans[-1] == -astroid:
                    ans.pop()
                    break
                elif ans[-1] < -astroid:
                    ans.pop()
                    continue
                elif ans[-1] > -astroid: break
            else: ans.append(astroid)   
        return ans