###########################################
# Let's Have Some Fun
# File Name: 220.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Sep  1 11:32:42 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#220. Contains Duplicate III

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # similar to question 219 (t = 0)
        # we find the 'duplicates' nums[i], nums[j] in a window of size k
        # 'duplicates' is defined as
        # | nums[i] - nums[j] | <= t
        # | nums[i]//t - nums[j]//t | <= 1
        # Therefore,
        # -1 <= nums[i]//t - nums[j]//t <= 1
        # Since nums[k]//t is an integer
        # nums[i]//t is in {(nums[j]//t)+1, nums[j]//t, (nums[j]//t)-1}
        if k < 1 or t < 0: return False
        dt = collections.OrderedDict() # with size k
        N = len(nums)
        for i in range(N):
            n = nums[i]
            key = n // t if t else n
            for m in [key-1, key, key+1]:
                if m in dt and abs(dt[m] - n) <= t:
                    return True
            if len(dt) >= k:
                dt.popitem(last=False) # FIFO, first in first out
            dt[key] = n

        return False




