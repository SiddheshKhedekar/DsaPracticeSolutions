# Keys and Rooms -> Python3

'''
Explanation: Use array of traversed rooms and set for uniqueness. Traverse room starting from first 
and add unique room in set. If length of set and rooms is same then true otherwise false.
'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dfs = [0]
        seen = set(dfs)
        while dfs:
            i = dfs.pop()
            for j in rooms[i]:
                if j not in seen:
                    dfs.append(j)
                    seen.add(j)
                    if len(seen) == len(rooms): return True
        return False