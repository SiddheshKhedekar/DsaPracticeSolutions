# Design HashMap -> Python3

'''
Explanation: Implementation using array where in init set data to [none] * maxsize. In put set 
data[key] to value. In remove set data[key] to none. In get return data[key] if it is not none 
else -1.
'''

class MyHashMap:

    def __init__(self):
        self.data = [None] * 1000001

    def put(self, key: int, value: int) -> None:
        self.data[key] = value

    def get(self, key: int) -> int:
        return self.data[key] if self.data[key] != None else -1

    def remove(self, key: int) -> None:
        self.data[key] = None