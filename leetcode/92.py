###########################################
# Let's Have Some Fun
# File Name: 92.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 17 Aug 00:43:26 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 92. Reverse Linked List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        h = ListNode(0)
        h.next = head
        i = 0
        p = h
        r = None
        reverse_head = None # head of reverse part
        while p:
            if i >= m and i<=n:
                q = p.next
                p.next = reverse_head
                reverse_head = p
                p = q
                i += 1
                continue
            elif i == m-1:
                r = p
            elif i > n:
                break
            p = p.next
            i += 1

        r.next.next = p # r.next becomes the last node in reverse_head
        r.next = reverse_head
        return h.next

