# Text Justification -> Python3

'''
Explanation: Set ans, crnt as empty array and freq as 0 then loop on wrd in words. Then check if 
freq + len wrd + len crnt is greater than max length to run loop for i in range of maxwidth - freq 
and inside increment the value at crnt i % len crnt - 1 or 1 by extra space. Before exiting if 
append crnt after join in ans and reset crnt and freq. Add wrd as array in crnt and increment freq 
by len of wrd. Finally return ans after adding joined crnt that is left justified on maxWidth. 
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans, crnt, freq = [], [], 0
        for wrd in words:
            if freq + len(wrd) + len(crnt) > maxWidth:
                for i in range(maxWidth - freq):
                    crnt[i % (len(crnt) - 1 or  1)] += ' '
                ans.append(''.join(crnt))
                crnt, freq = [], 0
            crnt += [wrd]
            freq += len(wrd)
        return ans + [' '.join(crnt).ljust(maxWidth)]