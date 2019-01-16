###########################################
# Let's Have Some Fun
# File Name: 653.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 15 20:24:21 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 653. Two Sum IV - Input is a BST

from queue import Queue

class Solution:
    # brutal method with BFS
    def findTarget1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        q = Queue()
        q.put(root)
        lst = set([])
        while not q.empty():
            nd = q.get()
            if k - nd.val in lst:
                return True
            lst.add(nd.val)
            if nd.left:
                q.put(nd.left)
            if nd.right:
                q.put(nd.right)
        return False

    # DFS with inOrder
    def findTarget2(self, root, k):
        lst = set([])
        st = []
        nd = root
        while len(st) or nd:
            while nd:
                st.append(nd)
                nd = nd.left
            nd = st.pop()
            lst.add(nd.val)
            nd = nd.right
        i = 0
        j = len(lst)-1
        while i<j:
            if lst[i] + lst[j] < k:
                i += 1
            elif lst[i] + lst[j] > k:
                j -= 1
            else:
                return True
        return False


