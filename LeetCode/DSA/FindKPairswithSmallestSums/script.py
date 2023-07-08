# Find K Pairs with Smallest Sums -> Python3

'''
Explanation: We start off only with the very first pair at the top-left corner of the matrix, and 
expand from there as needed. Whenever a pair is chosen into the output result, the next pair in the 
row gets added to the priority queue of current options. Also, if the chosen pair is the first one 
in its row, then the first pair in the next row is added to the queue. For this we implement push 
function and call it from loop in main function.
'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        que, prs = [], []
        def push(x, y):
            if x < len(nums1) and y < len(nums2):
                heapq.heappush(que, [nums1[x] + nums2[y], x, y])
        push(0, 0)
        while que and len(prs) < k:
            _, x, y = heapq.heappop(que)
            prs.append([nums1[x], nums2[y]])
            push(x, y + 1)
            if y == 0: push(x + 1, 0)
        return prs