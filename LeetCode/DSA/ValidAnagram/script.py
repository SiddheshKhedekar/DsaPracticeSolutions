# Valid Anagram -> Python3

'''
Explanation: Set freq using default dict and loop on s to increment freq at i then loop on t to 
decrement freq at i. Finally loop on freq values to check if i is not 0 to return false else at end 
return true.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = defaultdict(int)
        for i in s: freq[i] += 1
        for i in t: freq[i] -= 1
        for i in freq.values():
            if  i != 0: return False
        return True