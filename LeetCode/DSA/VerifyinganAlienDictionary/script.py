# Verifying an Alien Dictionary -> Python3

'''
Explanation: Get the order as key in a dictionary with its index saved as value. Create a new array 
where the alphabet in word mapping in dictionary can be saved by using two loops. Use zip or just 
compare the ith index with i+1 and return false if order is not asc.
'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        return words == sorted(words, key=lambda w: list(map(order.index, w)))