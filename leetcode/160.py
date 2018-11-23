###########################################
# Let's Have Some Fun
# File Name: 160.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Nov 21 00:40:17 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 160. Intersection of Two Linked Lists

import math
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    # cal length of headA and headB
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = 0
        l2 = 0
        pA = headA
        pB = headB
        while(pA):
            l1 += 1
            pA = pA.next
        while(pB):
            l2 += 1
            pB = pB.next
        if l1 == 0 or l2 == 0:
            return None
        n = l1 - l2
        if l1 > l2:
            pA = headA
            pB = headB
            while(n):
                pA = pA.next
                n -= 1
        elif l1 < l2:
            n = -n
            pB = headB
            pA = headA
            while(n):
                pB = pB.next
                n -= 1
        else:
            pA = headA
            pB = headB

        while pA and pB:
            if pA == pB:
                return pA
            else:
                pA = pA.next
                pB = pB.next
        return None

    # traverse A and B, one node each step
    # when A reaches the end, move to the head of B
    # when B reaches the end, move to the head of A
    def getIntersectionNodeStandard(self, headA, headB):
        pA = headA
        pB = headB
        tailA = None
        tailB = None
        if pA == None or pB == None:
            return None
        while True:
            if pA == pB:
                return pA
            if pA.next == None:
                tailA = pA
                pA = headB
            else:
                pA = pA.next
            if pB.next == None:
                tailB = pB
                pB = headA
            else:
                pB = pB.next
            if tailA != None and tailB != None:
                if tailA != tailB:
                    return None


if __name__ == '__main__':
    s = Solution()


