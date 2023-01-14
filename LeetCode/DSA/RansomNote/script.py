# Ransom Note -> Python3

'''
Explanation: Get dictionary of magazine and ransom note. Check if key exists and count is same or 
more in magazine as in ransom note.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rfreq, qfreq, flg = collections.Counter(ransomNote), collections.Counter(magazine), 0
        for i in rfreq:
            if i not in qfreq.keys() or rfreq[i] > qfreq[i]: flg = 1
        return flg == 0