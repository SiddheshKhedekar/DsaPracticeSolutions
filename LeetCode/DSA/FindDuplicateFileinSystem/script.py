# Find Duplicate File in System -> Python3

'''
Explanation: Use hashmap. Initialize a default dift from collections library that takes in list 
param. Loop over line in paths and get data by splitting the line using function. Set root to 
data[0] and loop overfile in data[1:]. Partition file on ( using function and save in name, _ and 
content. In memory[content[:-1]] append the root/name. Return the x in m.values if len x is > 1.
'''

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)
        for line in paths:
            data = line.split()
            root = data[0]
            for file in data[1:]:
                name, _, content = file.partition('(')
                m[content[:-1]].append(root+'/'+name)
        return [x for x in m.values() if len(x) > 1]