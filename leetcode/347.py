###########################################
# Let's Have Some Fun
# File Name: 347.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Dec 31 18:28:07 2018
###########################################
#coding=utf-8
#!/usr/bin/python
import heapq
import collections

class Solution:
    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dt = {}
        ret = []
        for n in nums:
            dt[n] = dt.get(n, 0) - 1
        hp = [(dt[k], k) for k in dt.keys()]
        heapq.heapify(hp) # min heap
        for i in range(k):
            ret.append(heapq.heappop(hp)[1])
        return ret

    # Use collections and nlargest
    def topKFrequent2(self, nums, k):
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)




if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent2([1,1,1,3,3,2],2))
    print(s.topKFrequent2([1], 1))
