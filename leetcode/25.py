###########################################
# Let's Have Some Fun
# File Name: 25.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Sep 16 08:45:55 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#25. Reverse Nodes in k-Group

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        ret_head = ListNode(0)
        ret_tail = ret_head
        p = head
        tmp_head = None
        tmp_tail = None
        i = 0
        while True:
            if not p: break
            if i % k == 0:
                if tmp_head:
                    ret_tail.next = tmp_head
                    ret_tail = tmp_tail
                tmp_head, tmp_tail = p, p
                p = p.next
                tmp_tail.next = None
            else:
                bak = p.next
                p.next = tmp_head
                tmp_head = p
                p = bak
            i += 1

        p = None
        if i % k != 0:
            while tmp_head:
                # reverse tmp_head and add to ret_tail
                bak = tmp_head.next
                tmp_head.next = p
                p = tmp_head
                tmp_head = bak
            ret_tail.next = p
        else:
            ret_tail.next = tmp_head

        return ret_head.next

