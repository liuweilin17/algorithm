###########################################
# Let's Have Some Fun
# File Name: 23.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Sep 15 22:15:09 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#23. Merge k Sorted Lists

import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # time: O(logK * N), K lists and N nodes in total
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        N = len(lists)
        if N == 0: return None
        # Build Heap
        H = []
        for i in range(N):
            nd = lists[i]
            if nd:
                H.append((lists[i].val, id(lists[i]), lists[i]))
        heapq.heapify(H)

        head = ListNode(0)
        p = head
        while H:
            v, id_nd, nd = heapq.heappop(H)
            if nd.next:
                heapq.heappush(H, (nd.next.val, id(nd.next), nd.next))
            nd.next = None
            p.next = nd
            p = p.next

        return head.next


