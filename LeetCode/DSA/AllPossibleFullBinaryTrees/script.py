# All Possible Full Binary Trees -> Python3

'''
Explanation: Build answer backwards using recursive call and avoid problem of multiple ways filling 
out left branch by not always cloning by doing it for each step except the last one. In main 
function check valid n and initialize ans thn loop on range in skips of 2 and set lb ,rb as 
recursive call to itself then loop on lb and inside loop on rb to call clone and set ans.
'''

class Solution:
    def clone(self, tree):
        if not tree: return None
        new_tree = TreeNode(0)
        new_tree.left = self.clone(tree.left)
        new_tree.right = self.clone(tree.right)
        return new_tree
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0: return []
        elif n == 1: return [TreeNode(0)]
        ans = []
        for x in range(2, n + 1, 2):
            lb = self.allPossibleFBT(x - 1)
            rb = self.allPossibleFBT(n - x)
            for lcnt, l in enumerate(lb, 1):
                for rcnt, r in enumerate(rb, 1):
                    tree = TreeNode(0)
                    tree.left = self.clone(l) if rcnt < len(rb) else l
                    tree.right = self.clone(r) if lcnt < len(lb) else r
                    ans.append(tree)
        return ans