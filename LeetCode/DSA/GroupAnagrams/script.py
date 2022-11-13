# Group Anagrams -> Python3

'''
Explanation: Need to define a default dict of list. Then iterate on the strs array append to the 
dict at tuple sorted word position the word. Finally return the list of dict values.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word) 
        return list(letters_to_words.values())