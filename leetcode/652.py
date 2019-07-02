# 652. Find Duplicate Subtrees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root: return []
        ret = []
        # use dfs to find the string representation of all subtrees
        dt = collections.defaultdict(int)
        def dfs(nd):
            if not nd: 
                return "#"
            vec = str(nd.val) + dfs(nd.left) + dfs(nd.right)
            dt[vec] += 1
            if dt[vec] == 2:
                ret.append(nd)
                
            return vec
        
        dfs(root)
        return ret
                
