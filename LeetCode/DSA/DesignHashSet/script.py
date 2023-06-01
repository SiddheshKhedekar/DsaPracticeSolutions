# Design HashSet -> Python3

'''
Explanation: In init set data as array of arrays of maxrange then define eval hash as return of key 
after performing hashing. In add get indx by eval hash of key and if key not in data at index 
append key at same index. In remove eval hash in index and check if key in data at index and 
remove. In contains eval hash in index and return key in data at index.
'''

class MyHashSet:
    def eval_hash(self, key):
        return ((key * 1031237) & (1 << 20) - 1) >> 5
    def __init__(self):
        self.data = [[] for _ in range(1<<15)]
    def add(self, key: int) -> None:
        indx = self.eval_hash(key)
        if key not in self.data[indx]: self.data[indx].append(key)
    def remove(self, key: int) -> None:
        indx = self.eval_hash(key)
        if key in self.data[indx]: self.data[indx].remove(key)
    def contains(self, key: int) -> bool:
        indx = self.eval_hash(key)
        return key in self.data[indx]