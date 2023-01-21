# Restore IP Addresses -> Python3

'''
Explanation: Write a dfs function that takes in a string, index, path and answer array as input. 
For index > 4 return, when 4 and string empty append path except last character to answer. In a for 
loop from 1 to end of length check for ip conditions and call dfs function with updated inputs. 
'''

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(string, index, path, ans):
            if index > 4: return
            if index == 4 and not string:
                ans.append(path[:-1])
                return
            for x in range(1, len(string)+1):
                if string[:x] == '0' or (string[0] != '0' and int(string[:x]) < 256):
                    dfs(string[x:], index+1, path+string[:x]+".", ans)
        dfs(s, 0, "", ans)
        return ans