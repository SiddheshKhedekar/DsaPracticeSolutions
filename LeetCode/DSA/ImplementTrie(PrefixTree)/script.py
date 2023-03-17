# Implement Trie (Prefix Tree) -> Python3

'''
Explanation: Define a tnode class with init consisting of word set to false and dict of children. 
Inside trie class define init with root set to tnode. In add set node to root and then loop on i in 
word to check if not i in node children then set node children i to new tnode. Set node to its 
children i and out of loop set node word to true. Inside search do same except in if condition 
return false and at end of loop return the node word. For start run loop on prefix, in condition 
return false and outside loop return true.
'''

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.children: node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True
    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.children: return False
            node = node.children[i]
        return node.word
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node.children: return False
            node = node.children[i]
        return True