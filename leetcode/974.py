###########################################
# Let's Have Some Fun
# File Name: 974.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue 28 May 20:54:58 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#974. Subarray Sums Divisible by K

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A: return 0
        N = len(A)
        count = 0
        # cummutive sum
        sum_arr = [0] * (N+1)
        dt = collections.defaultdict(int)
        dt[0] = 1 # notice this is necessary
        for i in range(1, N+1):
            sum_arr[i] = sum_arr[i-1] + A[i-1]
            mod = sum_arr[i] % K
            if mod in dt: # find the number of sum with same mod
                count += dt[mod]
            dt[mod] += 1

        return count
