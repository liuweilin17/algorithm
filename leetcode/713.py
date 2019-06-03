###########################################
# Let's Have Some Fun
# File Name: 713.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed 29 May 21:27:49 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#713. Subarray Product Less Than K

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left, right = 0, 0
        product = 1
        count = 0

        #sliding window
        while left<=right and left<N:
            if product < k:
                if right < N:
                    product *= nums[right]
                    right += 1
                else:
                    count += (right-left)
                    left += 1
            else:
                if right > left:
                    count += (right - left - 1)
                product /= nums[left]
                left += 1

        return count

