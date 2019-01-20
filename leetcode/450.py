###########################################
# Let's Have Some Fun
# File Name: 450.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 20 13:25:08 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None

        # preorder dfs
        st = []
        st.append((root, None, 0))
        while len(st):
            nd, parent, flag = st.pop()
            if nd.val == key:
                # remove
                if not nd.left and not nd.right:
                    if flag == 1:
                        parent.right = None
                    elif flag == -1:
                        parent.left = None
                    else:
                        root = None
                elif nd.left and nd.right:
                    # find the the leftist nd of nd.right
                    r = nd.right
                    l = nd.left
                    tmp = l.right
                    while r.left:
                        r = r.left
                    r.left = tmp
                    l.right = nd.right
                    if flag == 1:
                        parent.right = l
                    elif flag == -1:
                        parent.left = l
                    else:
                        root = l
                else:
                    if flag == 1:
                        parent.right = nd.left if nd.left else nd.right
                    elif flag == -1:
                        parent.left = nd.left if nd.left else nd.right
                    else:
                        root = nd.left if nd.left else nd.right
                break
            if nd.right:
                st.append((nd.right, nd, 1))
            if nd.left:
                st.append((nd.left, nd, -1))

        return root


