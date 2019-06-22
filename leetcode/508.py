###########################################
# Let's Have Some Fun
# File Name: 508.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri 21 Jun 09:30:50 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#508. Most Frequent Subtree Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []

        dt = collections.defaultdict(int)

        # post order dfs
        # return the sum of nodes of nd
        def dfs(nd):
            if not nd: return 0
            sum1 = dfs(nd.left)
            sum2 = dfs(nd.right)
            sumV = nd.val + sum1 + sum2
            dt[sumV] += 1
            return sumV

        dfs(root)
        ret = []
        maxV = max(dt.values())
        for k in dt:
            if dt[k] == maxV:
                ret.append(k)

        return ret


