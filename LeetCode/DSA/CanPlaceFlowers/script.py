# Can Place Flowers -> Python3

'''
Explanation: Initialize zros to 1 and res as 0 then loop on flowerbed to check if flower is 0 and 
increment zros else increment res by zros - 1 // 2 then set zros to 0. Finally return if the sum of 
res and zros // 2 is greater than or same as n.
'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zros, res = 1, 0
        for flower in flowerbed:
            if flower == 0: zros += 1
            else:
                res += (zros - 1) // 2
                zros = 0
        return res + zros // 2 >= n