# Dota2 Senate -> Python3

'''
Explanation: Initialize que as deque, people as [0,0] and same for bans. For member in senate run 
loop and set i to member == "R" then increment people at i by 1 and append i to que. Run loop while 
all people and set i by popleft que then decrement people at by 1 and if bans at i exists then 
decrement it by 1. Else increment bans at i ^ 1 by 1 then append i to que and increment people at i 
by 1. Finally return radiant if people at 1 exists else dire.
'''

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        que, people, bans = deque(), [0, 0], [0, 0]
        for member in senate:
            i = member == 'R'
            people[i] += 1
            que.append(i)
        while all(people):
            i = que.popleft()
            people[i] -= 1
            if bans[i]: bans[i] -= 1
            else:
                bans[i^1] += 1
                que.append(i)
                people[i] += 1
        return "Radiant" if people[1] else "Dire"