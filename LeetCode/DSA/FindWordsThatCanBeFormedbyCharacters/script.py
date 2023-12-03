# Find Words That Can Be Formed by Characters -> Python3

'''
Explanation: Count the characters in chars in array cnt, then for each wrd in words check if cnt 
has enough to cover it.
'''

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sm, cnt = 0, collections.Counter
        chrCnt = cnt(chars)
        for wrd in words:
            wrdCnt = cnt(wrd)
            if all(wrdCnt[char] <= chrCnt[char] for char in wrdCnt): sm += len(wrd)
        return sm