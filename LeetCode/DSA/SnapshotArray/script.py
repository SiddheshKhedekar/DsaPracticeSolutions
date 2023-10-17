# Snapshot Array -> Python3

'''
Explanation: Set arr as array of array with initial items -1, 0 for range len and global snap_id as 
0. Then in set append array of snap_id, val in array at index. In snap increment snap_id by 1 and 
return snap_id - 1. In get set the indx as bisect of arr at index and arr of snap_id - 1 and return 
the arr  at index indx 1.
'''

class SnapshotArray:
    def __init__(self, length: int):
        self.arr, self.snap_id = [[[-1, 0]] for _ in range(length)], 0
    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id, val])
    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
    def get(self, index: int, snap_id: int) -> int:
        indx = bisect.bisect(self.arr[index], [snap_id + 1]) - 1
        return self.arr[index][indx][1]   