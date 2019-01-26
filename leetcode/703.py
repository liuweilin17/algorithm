###########################################
# Let's Have Some Fun
# File Name: 703.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Jan 25 21:32:31 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 703. Kth Largest Element in a Stream

import heapq

class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.kLargest = heapq.nlargest(k, nums)
        heapq.heapify(self.kLargest)
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.kLargest) < self.k: # notice!!!, the len of kLargest may less than k
            heapq.heappush(self.kLargest, val)
        elif val > self.kLargest[0]:
            heapq.heappushpop(self.kLargest, val)
        else: pass
        return self.kLargest[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
