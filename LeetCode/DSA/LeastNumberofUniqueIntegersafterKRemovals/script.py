# Least Number of Unique Integers after K Removals -> Python3

'''
Explanation: First save the frequency of all numbers in list as f then save the freq of f values in 
cntr. Loop for range 1 to len nums + 1 and check if k is greater than key * cntr at key to 
decrement k by it and decrement rem by cntr at key else return rem - k floor div by key and at the 
end return rem.
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        f = Counter(arr)
        cntr, rem = Counter(f.values()), len(f)
        for key in range(1, len(arr) + 1):
            if k >= key * cntr[key]:
                k -= key * cntr[key]
                rem -= cntr[key]
            else: return rem - k // key
        return rem