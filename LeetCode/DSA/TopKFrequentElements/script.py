# Top K Frequent Elements -> Python3

'''
Explanation: Initialize bckt as array containing arrays of len num. Then iterate n,f on counter 
items of nums and append n to bckt at -f. Finally return first k items in list of itertools chain 
*bckt.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bckt = [[] for _ in nums]
        for n, f in Counter(nums).items(): bckt[-f].append(n)
        return list(itertools.chain(*bckt))[:k]