# Maximize the Confusion of an Exam -> Python3

'''
Explanation: Set mxf as counter and both x, cnt as 0 then run loop for y on range of len answerkey. 
Inside increment cnt at answerkey at y by 1 and set mxf as max of mxf and cnt at answerkey at y. 
Then check if y - x + 1 is greater than mxf + k and decrement the cnt at answerkey at x by 1 and 
increment x by 1. Finally return the len of answerkey - x.
'''

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        mxf, x, cnt = 0, 0, collections.Counter()
        for y in range(len(answerKey)):
            cnt[answerKey[y]] += 1
            mxf = max(mxf, cnt[answerKey[y]])
            if y - x + 1 > mxf + k:
                cnt[answerKey[x]] -= 1
                x += 1
        return len(answerKey) - x