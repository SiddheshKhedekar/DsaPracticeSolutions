# Fruit Into Baskets -> Python3

'''
Explanation: Initialize a dictionary of count and i as 0. Then run loop on enumerated tree and set 
count at v to 1 + its value in count or 0. Then check if len count is greater than 2 and decrement 
count at fruits i by 1. Then check if count at fruits i is 0 and delete it. Increment i by 1 and 
return j - i + 1. 
'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count, i = {}, 0
        for j, v in enumerate(fruits):
            count[v] = count.get(v,0) + 1
            if len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0: del count[fruits[i]]
                i += 1
        return j - i + 1