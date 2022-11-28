# Find Players With Zero or One Losses -> Python3

'''
Explanation: Use a hashmap to save the winner and loser count in a loop. Use another loop to check 
the count of wins and append in array. Finally return the sorted arrays.
'''

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        allwin, oneloss, stats = [], [], {}
        for winner, loser in matches:
            stats[winner] = stats.get(winner, 0)
            stats[loser] = stats.get(loser, 0) + 1
        for i, j in stats.items():
            if j == 0: allwin.append(i)
            if j == 1: oneloss.append(i)
        return [sorted(allwin), sorted(oneloss)]