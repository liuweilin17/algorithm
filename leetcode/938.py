###########################################
# Let's Have Some Fun
# File Name: 938.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 11 13:14:32 2018
###########################################
#coding=utf-8
#!/usr/bin/python

import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # This method is easy to come up with, but without using the properties of BST
    def rangeSumBST1(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        sum = 0
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            n = q.get()
            v = n.val
            if v >= L and v <= R:
                sum += v
            if n.left != None:
                q.put(n.left)
            if n.right != None:
                q.put(n.right)
        return sum

    # recursive method
    def rangeSumBST2(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def dfs(nd):
            if not nd:
                return
            if nd.val <= R and nd.val >= L:
                self.ans += nd.val
            if nd.val < R:
                dfs(nd.right)
            if nd.val > L:
                dfs(nd.left)
        self.ans = 0
        dfs(root)
        return self.ans
    
    # iterative method
    def rangeSumBST3(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return []

        ret = 0
        st = []
        st.append(root)
        while len(st):
            nd = st.pop()
            if nd.val >= L and nd.val <= R:
                ret += nd.val
            if nd.val > L and nd.left:
                st.append(nd.left)
            if nd.val < R and nd.right:
                st.append(nd.right)

        return ret

if __name__ == "__main__":
    s = Solution(i)
