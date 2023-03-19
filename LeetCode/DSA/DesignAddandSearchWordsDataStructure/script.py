# Design Add and Search Words Data Structure -> Python3

'''
Explanation: At init set children as array of None * 26 for num of alphabets and fladeow as false. 
in add set crnt as self and loop on word, check if none at children of crnt at index based on ord 
and create new wordDict then set crnt to children of crnt at index and set flag as true. In search 
set crnt as self and loop of len of word, if w is . then loop on crnt children to check if it is 
not none and if search of remaining words returns true else outside the inner loop retturn false. 
Check if none at children of crnt at index based on ord and return false then set crnt to children 
of crnt at index finally return if crnt not none and crnt flag value.
'''

class WordDictionary:
    def __init__(self):
        self.children = [None] * 26
        self.flagEow = False
    def addWord(self, word: str) -> None:
        crnt = self
        for w in word:
            if crnt.children[ord(w) - ord('a')] == None: 
                crnt.children[ord(w) - ord('a')] = WordDictionary()
            crnt = crnt.children[ord(w) - ord('a')]
        crnt.flagEow = True
    def search(self, word: str) -> bool:
        crnt = self
        for x in range(len(word)):
            w = word[x]
            if w == '.':
                for ch in crnt.children:
                    if ch != None and ch.search(word[x+1:]): return True
                return False
            if crnt.children[ord(w) - ord('a')] == None: return False
            crnt = crnt.children[ord(w) - ord('a')]
        return crnt != None and crnt.flagEow