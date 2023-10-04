# Remove Colored Pieces if Both Neighbors are the Same Color -> Python3

'''
Explanation: Loop on z in range 1 to len - 1 and check if three corresponding elements are same 
then check if character a to increment x else y by 1 which were 0 at init. Finally at end of loop 
return if x greater than y.
'''

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        x = y = 0
        for z in range(1, len(colors) - 1):
            if colors[z - 1] == colors[z] == colors[z + 1]:
                if colors[z] == 'A': x += 1
                else: y += 1
        return x > y