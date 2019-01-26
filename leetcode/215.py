###########################################
# Let's Have Some Fun
# File Name: 215.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Jan 25 20:27:23 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 215. Kth Largest Element in an Array

import heapq

class Solution:
    # use partition method from the quick sort
    def partition(self, arr):
        n = len(arr)
        pivot = arr[n - 1]
        i = -1
        for j in range(n):
            if arr[j] >= pivot:
                i += 1
                tmp = arr[i]
                arr[i] = arr[j]
                arr[j] = tmp
        return i
    # O(n) average, O(n2) worst case
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        r = self.partition(nums)
        if r < k - 1:
            return self.findKthLargest(nums[r + 1:], k - 1 - r)
        elif r > k - 1:
            return self.findKthLargest(nums[:r], k)
        else:
            return nums[r]

    # use heap sort
    def findKthLargest2(self, nums, k):
        n = len(nums)
        heapq.heapify(nums)
        for i in range(n-k):
            heapq.heappop(nums)
        return heapq.heappop(nums)

if __name__ == '__main__':
    a = [3,2,1,5,6,4]
    k = 2
    s = Solution()
    print(s.findKthLargest2(a, 2))
