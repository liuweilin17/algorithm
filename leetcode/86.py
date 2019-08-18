###########################################
# Let's Have Some Fun
# File Name: 86.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri 16 Aug 11:12:46 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 86. Partition List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # ret: empty head of new list
        # r: traverse the new list
        ret = ListNode(0)
        r = ret

        # h: empty head of 'head'
        # p: traverse the 'head'
        h = ListNode(0)
        h.next = head
        p = h
        while p and p.next:
            if p.next.val < x:
                # extract p.next(q) and append after r
                q = p.next
                p.next = q.next
                q.next = None
                r.next = q
                r = r.next
            else:
                p = p.next

        # merge ret (< x) and h(>=x)
        r.next = h.next
        return ret.next

