###########################################
# Let's Have Some Fun
# File Name: 865.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu 20 Jun 17:31:53 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#865. Smallest Subtree with all the Deepest Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # My method
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root: return None

        ret = None
        deepest = 0
        parents = {}
        # dfs pre order, root->left->right
        st = [(root, 1)]
        parents[root] = None # This is essential !!!
        while st:
            nd, depth = st.pop()
            if not nd.left and not nd.right:
                if depth > deepest:
                    ret = nd
                    deepest = depth #Notice updating the 'deepest' variable !!!
                elif depth == deepest:
                    paths = []
                    p = nd
                    while p:
                        paths.append(p)
                        p = parents[p]
                    while True:
                        if ret in paths:
                            break
                        else:
                            ret = parents[ret]
                else: pass

            if nd.left:
                st.append((nd.left, depth+1))
                parents[nd.left] = nd
            if nd.right:
                st.append((nd.right, depth+1))
                parents[nd.right] = nd

        return ret

    def subtreeWithAllDeepest2(self, root: TreeNode) -> TreeNode:
        if not root: return None

        maximum_depth = 0
        depth_dt = {}

        def dfs(nd, depth):
            depth_dt[nd] = depth
            if nd.left:
                dfs(nd.left, depth+1)
            if nd.right:
                dfs(nd.right, depth+1)

        dfs(root, 1)
        maximum_depth = max(depth_dt.values())

        def helper(nd):
            if not nd or depth_dt[nd] == maximum_depth:
                return nd
            L = helper(nd.left)
            R = helper(nd.right)

            if L and R: return nd
            elif L:
                return L
            elif R:
                return R
            else: pass

        return helper(root)
