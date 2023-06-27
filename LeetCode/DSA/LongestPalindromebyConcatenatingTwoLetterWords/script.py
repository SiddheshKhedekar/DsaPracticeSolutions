# Longest Palindrome by Concatenating Two Letter Words -> Python3

'''
Explanation: Counter using 2 dim array of 26, iterate on words and check set ab using ord check if 
counter w[b a] exists and increment count by 4 then decrement counter ba else increment counter ab 
iterate on counter again and check for i,i and increment count by 2 and break. Finally return 
counter outside loop.
'''

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        counter, ans = [[0] * 26 for _ in range(26)], 0
        for w in words:
            a, b = ord(w[0]) - ord('a'), ord(w[1]) - ord('a')
            if counter[b][a]:
                ans+=4
                counter[b][a]-=1
            else: counter[a][b]+=1
        for i in range(26):
            if counter[i][i]:
                ans+=2
                break
        return ans