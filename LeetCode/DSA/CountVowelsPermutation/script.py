# Count Vowels Permutation -> Python3

'''
Explanation: First initialize a, e, i, o, u as 1 and then loop for range n - 1.Each vowel allows 
some number of subsequent characters. These rules are like trees. Inside loop assign the values to 
vars based on the rules defined. Finally return the sum of all vars mod by given value.
'''

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o
        return (a + e + i + o + u) % (10 ** 9 + 7)