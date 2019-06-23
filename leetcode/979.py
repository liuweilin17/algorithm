###########################################
# Let's Have Some Fun
# File Name: 979.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon 17 Jun 22:26:50 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#979. Distribute Coins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ret = 0
        
        # the number of coins could be given to the nd's parent
        def dfs(nd):
            if not nd: return 0
            L = dfs(nd.left) # the number of coins given by nd.left
            R = dfs(nd.right) # the number of coins given by nd.right
            
            self.ret += abs(L) + abs(R) # number of coins(moves) from left and right subtree
            
            return nd.val - 1 + L + R # the number of coins could be given to nd's parent
        
        dfs(root)
        return self.ret
