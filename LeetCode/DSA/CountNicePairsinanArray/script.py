# Count Nice Pairs in an Array -> Python3

'''
Explanation: Try to simplify the condition where it comes down to finding the count of the pairs 
where diff is the same. First set ans and cnt as 0, counter then loop on x in nums and set y as the 
int of str from x in reverse. Increment ans by cnt of x-y and increment cnt at x-y by 1 and finally 
return ans mod by given value.
'''

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ans, cnt = 0, Counter()
        for x in nums:
            y = int(str(x)[::-1])
            ans += cnt[x - y]
            cnt[x - y] += 1
        return ans % (10 ** 9 + 7)