# Top K Frequent Words -> Python3

'''
Explanation: Get frequency using Counter and return heapq nsmallest based on negative word 
frequency.
'''

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        return heapq.nsmallest(k,freq,key=lambda word:(-freq[word],word))