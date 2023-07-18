# Word Ladder -> Python3

'''
Explanation: Initialize wordlist as set of wordlist and q as deque of array with arrayitem 
beginword, 1 then run loop while q. Inside set wrd, l as popleft on q then check if wrd is endword 
and return 1. Then run loop for x in range len wrd and inside run foop for char in all alphabets. 
Set nxtword as word  upto x + char + word from x+1 to end and check if nxtwrd is in wrdlist. Remove 
nxtwrd from wrdlist and append nxtwrd with l+1 as arrayitem in q.
'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wrdLst, q = set(wordList), deque([[beginWord, 1]])
        while q:
            wrd, l = q.popleft()
            if wrd == endWord: return l
            for x in range(len(wrd)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    nxtWrd = wrd[:x] + char + wrd[x + 1:]
                    if nxtWrd in wrdLst:
                        wrdLst.remove(nxtWrd)
                        q.append([nxtWrd, l + 1])
        return 0