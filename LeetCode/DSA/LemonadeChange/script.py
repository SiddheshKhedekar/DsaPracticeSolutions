# Lemonade Change -> Python3

'''
Explanation: Set five and ten to 0 run loop for i in bills. If i = 5 then increment 5 by 1 elseif 
bill = 10 check if not five return false, decrement five by 1 and increment 10 by 1 finally in else 
check if ten and five and decrement 1 elseif five >=3 decrement 3 else return false out of loop 
return true.
'''

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = 0
        for bill in bills:
            if bill == 5: five+=1
            elif bill == 10:
                if not five: return False
                five-=1
                ten+=1
            else:
                if ten and five:
                    ten-=1
                    five-=1
                elif five >= 3: five-=3
                else: return False
        return True