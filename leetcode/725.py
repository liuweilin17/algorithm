###########################################
# Let's Have Some Fun
# File Name: 725.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Jan 21 17:56:06 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root: return [None] * k
        n = 0
        p = root
        while p:
            n += 1
            p = p.next

        ret = []
        p, q, r = root, None, None
        a = n % k
        b = n // k
        #print("{0},{1},{2},{3}".format(n, k, a, b))
        for i in range(k):
            if not p:
                ret.append(None)
            else:
                q = p

                for j in range(b-1):
                    q = q.next
                if i < a and b > 0: # notice!, when b==0, it should not have one more
                    q = q.next

                r = q.next
                q.next = None
                ret.append(p)
                p = r
        return ret

