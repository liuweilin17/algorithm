###########################################
# Let's Have Some Fun
# File Name: 1186.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Sep  8 09:16:06 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 1186. Maximum Subarray Sum with One Deletion

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        N = len(arr)
        dp1 = [0] * N # maximum sum ending at i, from 0,1,..,i
        dp1[0] = arr[0]
        for i in range(1, N):
            dp1[i] = max(dp1[i-1]+arr[i], arr[i])
        dp2 = [0] * N # maximum sum ending at i, from N-1, ..., i
        dp2[N-1] = arr[N-1]
        for i in range(N-2, -1, -1):
            dp2[i] = max(dp2[i+1]+arr[i], arr[i])
        
        ret = max(max(dp1), max(dp2))
        for i in range(1, N-1):
            ret = max(ret, dp1[i-1] + dp2[i+1])
            
        return ret
            
        
