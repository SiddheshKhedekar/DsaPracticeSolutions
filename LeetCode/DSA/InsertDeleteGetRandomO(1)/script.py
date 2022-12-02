# Insert Delete GetRandom O(1) -> Python3

'''
Explanation: In init use array for nums and dictionary for position. Get random using built in 
function and array length range. When inserting assign the position of val in dictionary. When 
removing swap the last value with the one to be removed and pop.
'''

class RandomizedSet:

    def __init__(self):
        self.nums, self.pos = [], {}

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            i, l = self.pos[val], self.nums[-1]
            self.nums[i], self.pos[l] = l, i
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        return self.nums[random.randint(0,len(self.nums)-1)]