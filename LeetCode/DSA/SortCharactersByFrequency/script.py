# Sort Characters By Frequency -> Python3

'''
Explanation: Get the frequencies using counter and in temp array populate characters on frequency 
index. In reverse order loop on range of initial word and inside loop on the individual chars for 
the frequency and populate the result by multiplying character and frequency.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        count, l, res = Counter(s), len(s), []
        temp = [[] for _ in range(l+1)]
        for i, f in count.items():
            temp[f].append(i)
        for f in range(l,-1,-1):
            for i in temp[f]:
                res.append(i*f)
        return "".join(res)