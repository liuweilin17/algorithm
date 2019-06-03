###########################################
# Let's Have Some Fun
# File Name: 560.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue 28 May 20:31:20 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#560. Subarray Sum Equals K

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = 0

        # cummutive sum
        # i > j, sum[i] - sum[j] represents all the subarray sum
        sum_arr = [0] * (N+1) # sum_arr[i] sum of 0,...,i-1
        dt = collections.defaultdict(int)
        dt[sum_arr[0]]=1 # notice this is essential
        for i in range(1, N+1):
            sum_arr[i] = sum_arr[i-1] + nums[i-1]
            if sum_arr[i] - k in dt: # notice all the sum_arr[j] in dt meets j < i
                count += dt[sum_arr[i]-k]
            dt[sum_arr[i]] += 1

        return count



