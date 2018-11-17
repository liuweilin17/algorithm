###########################################
# Let's Have Some Fun
# File Name: 141.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov 16 21:19:10 2018
###########################################
#coding=utf-8
#!/usr/bin/python
# 141. Linked List Cycle

from basics.LinkedList import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
		#使用两个速度不同的指针遍历数组，如果存在环，则两者会相遇
        slow = head
        fast = head.next
        while True:
            if slow == fast:
                return True
            if slow != None and fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next
            else:
                return False


if __name__ == '__main__':
    s = Solution()
