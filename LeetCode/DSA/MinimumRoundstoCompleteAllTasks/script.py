# Minimum Rounds to Complete All Tasks -> Python3

'''
Explanation: Get the frequencies of the tasks and return -1 if frequencies contain 1 else get sum 
by looping on frequencies and performing a+2 mod 3.
'''

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks).values()
        return -1 if 1 in freq else sum((a+2)//3 for a in freq)