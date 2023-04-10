# Kth Largest Element in an Array -> Python3

'''
Explanation: Check base condition and then implement quickselect. Set a pivot using random choice 
on nums and set left, right, mid and lengths of left, mid. If k is less or same as len of left then 
recursive call using left and k else if k is greater than lengths of left plus mid then recursive 
call right and k minus len of left minus len of mid else return mid at 0.
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums: return
        pvt = random.choice(nums)
        l = [i for i in nums if i > pvt]
        m = [i for i in nums if i == pvt]
        r = [i for i in nums if i < pvt]
        ll, lm = len(l), len(m)
        if k <= ll: return self.findKthLargest(l, k)
        elif k > ll + lm: return self.findKthLargest(r, k - ll - lm)
        else: return m[0]