###########################################
# Let's Have Some Fun
# File Name: 501.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Jan 18 19:51:07 2019
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
    # simply use in-order traverse and count the number of consecutive number
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        pre = None
        ret = []
        maxD = 0

        # in order traverse
        st = []
        nd = root
        count = 0
        while len(st) or nd:
            while nd:
                st.append(nd)
                nd = nd.left
            nd = st.pop()
            if pre != None:
                if nd.val == pre:
                    count += 1
                else:
                    if count == maxD:
                        ret.append(pre)
                    elif count > maxD:
                        ret = [pre]
                        maxD = count
                    count = 1
            else:
                count = 1
            pre = nd.val
            nd = nd.right

        if count == maxD:
            ret.append(pre)
        elif count > maxD:
            ret = [pre]

        return ret
