###########################################
# Let's Have Some Fun
# File Name: 523.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed 29 May 21:51:07 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#523. Continuous Subarray Sum

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if not nums: return False
        N = len(nums)

        length_one_num = 0
        for num in nums:
            if k == 0:
                if num == 0:
                    length_one_num += 1
            else:
                if num % k == 0:
                    length_one_num += 1

        #cummutive sum
        count = 0
        dt = collections.defaultdict(int)
        sum_arr = [0] * (N+1) # sum_arr[i] sum of 0, ..., i-1
        dt[0] = 1
        for i in range(1, N+1):
            sum_arr[i] = sum_arr[i-1] + nums[i-1]
            if k == 0:
                mod = sum_arr[i]
            else:
                mod = sum_arr[i] % k
            if mod in dt:
                count += dt[mod]
            dt[mod] += 1

        if count > length_one_num: # remove all the subarray with length one
            return True
        else:
            return False

