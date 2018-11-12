###########################################
# Let's Have Some Fun
# File Name: 237.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 11 23:27:14 2018
###########################################
#coding=utf-8
#!/usr/bin/python

from basics.LinkedList import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next != None:
            tmp = node.next
            node.val = node.next.val
            node.next = node.next.next
            del tmp
        else:
            del node
