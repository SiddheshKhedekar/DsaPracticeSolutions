# String Compression II -> Python3

'''
Explanation: Set @lru_cache to none, define function and return the counter(0, ‘’, 0, k). Inside 
counter function definition pass start, last, lc, left. Check if left < 0 return float inf, if 
start >= len(s) return 0, if s[start] = last set incr to 1 if lc = 1 or lc = 9 or lc = 99 else 0 
and return incr + counter(start +1, last, lc+1, left), in else set kc to 1 + 
counter(start+1,s[start], 1, left), dc to counter(start+1, last, lc, left+1) and return min(kc,dc).
'''

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def counter(start, last, last_count, left):
            if left < 0: return float('inf')
            if start >= len(s): return 0
            if s[start] == last:
                incr = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
                return incr + counter(start+1, last, last_count+1, left)
            else:
                keep_counter = 1 + counter(start+1, s[start], 1, left)
                del_counter = counter(start+1, last, last_count, left-1)
                return min(keep_counter, del_counter)
        return counter(0, '', 0, k)