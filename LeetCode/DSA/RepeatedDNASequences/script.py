# Repeated DNA Sequences -> Python3

'''
Explanation: Initialize sequences as defaultdict, in loop on length of s set sequences length for s 
from i to i+10. Then return as array the keys where values in sequences is greater than 1.
'''

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = collections.defaultdict(int)
        for i in range(len(s)):
            sequences[s[i:i+10]] += 1
        return [key for key, value in sequences.items() if value > 1]