###########################################
# Let's Have Some Fun
# File Name: 1191.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Sep 15 11:17:08 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1191. K-Concatenation Maximum Sum

class Solution:
    # notice that Kadane's algorithm is used to find the maximum sum of subarray in O(n) time
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        N = len(arr)
        if N < 1 or k < 1:
            return 0

        max_so_far = 0

        # case 1&2, max arr is in arr or in 2 arr
        new_arr = arr if k == 1 else arr * 2
        max_end_here = 0
        for a in new_arr:
            max_end_here = max(a, a+max_end_here)
            max_so_far = max(max_end_here, max_so_far)

        sum_v = sum(arr)
        if sum_v > 0 and k > 2: # several arr in the middle and we remove the smallest prefix and postfix of the first arr and last arr respectively
            print(">0")
            # minimum prefix sum
            min_pre = 0
            t = 0
            for i in range(N):
                t += arr[i]
                min_pre = min(min_pre, t)
            # minimum postfix sum
            min_post = 0
            t = 0
            for i in range(N-1, -1, -1):
                t += arr[i]
                min_post = min(min_post, t)
            print(min_pre, min_post)
            max_so_far = max(max_so_far, sum_v * k - min_pre - min_post)

        return max_so_far % (pow(10, 9) + 7)


