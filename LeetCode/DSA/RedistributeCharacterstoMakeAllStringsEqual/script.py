# Redistribute Characters to Make All Strings Equal -> Python3

'''
Explanation: First join array as string then create set of it. Then loop on x in sett and check if 
count of x in joinn mod by len of words is not 0 to return false otherwise on loop end return true.
'''

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        joinn = ''.join(words)
        sett = set(joinn)
        for x in sett:
            if joinn.count(x) % len(words) != 0 : return False
        return True