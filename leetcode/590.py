###########################################
# Let's Have Some Fun
# File Name: 590.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Jan 23 13:28:43 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 590. N-ary Tree Postorder Traversal

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    # recursive
    def postorder1(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        def dfs(nd, ret):
            if nd:
                for ch in nd.children:
                    if ch: dfs(ch, ret)
                ret.append(nd.val)

        ret = []
        dfs(root, ret)
        return ret
    # iterative
    # reverse preorder!!!!
    def postorder2(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        ret = []
        st = []
        st.append(root)
        while len(st):
            nd = st.pop()
            ret.append(nd.val)
            for ch in nd.children:
                if ch: st.append(ch)
        return list(reversed(ret))


