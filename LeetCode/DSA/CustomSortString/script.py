# Custom Sort String -> Python3

'''
Explanation: Save freq of chars in s then set res as array of freq pop of ch, 0 * ch for all ch in 
order. Loop for ch, val in freq items to append ch * val res in res and at end return string res.
'''

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = Counter(s)
        res = [freq.pop(ch, 0) * ch for ch in order]
        for ch, val in freq.items(): res.append(ch * val)
        return ''.join(res)