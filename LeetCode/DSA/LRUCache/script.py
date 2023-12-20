# LRU Cache -> Python3

'''
Explanation: Set size as capacity, cache prev and next as dict, head tail as ‘#’ ‘$’ and call 
connect with head and tail. In connect set next at a, prev at b as b, a. In delete call connect 
with prev and next at key then del prev next and cache at key. In append set cache at k as v call 
connect with prev at tail, k and again with k, tail then check if len of cache is greater than size 
to delete next at head. In get check if key not in cache to return -1, set val as the cache at key, 
call delete on key and call append key, val finally returning val. In put check if key in cache 
call delete on key then call append key, val.than money else return money.
'''

class LRUCache:
    def __init__(self, capacity: int):
        self.size, self.cache = capacity, {}
        self.next, self.prev = {}, {}
        self.head, self.tail = '#', '$'
        self.connect(self.head, self.tail)
    def connect(self, a, b): self.next[a], self.prev[b] = b, a
    def delete(self, key):
        self.connect(self.prev[key], self.next[key])
        del self.prev[key], self.next[key], self.cache[key]
    def append(self, k, v):
        self.cache[k] = v
        self.connect(self.prev[self.tail], k)
        self.connect(k, self.tail)
        if len(self.cache) > self.size: self.delete(self.next[self.head])
    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        val = self.cache[key]
        self.delete(key)
        self.append(key, val)
        return val
    def put(self, key: int, value: int) -> None:
        if key in self.cache: self.delete(key)
        self.append(key, value)