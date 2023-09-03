# Check If Two String Arrays are Equivalent -> Python3

'''
Explanation: Easy solution join arrays and check if string is equal. Space efficient solution to 
define generate function that yields all char in word in wordlist using nested for twice else 
yielding none. In main function zip the generate call for both arrays and check equivalence to 
return false else at end of loop return true.
'''

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        for c1, c2 in zip(self.generate(word1),self.generate(word2)):
            if c1 != c2: return False
        return True
    def generate(self,wordList):
        for word in wordList:
            for char in word: yield char
        yield None