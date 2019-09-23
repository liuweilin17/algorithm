###########################################
# Let's Have Some Fun
# File Name: 42.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Sep 20 10:09:29 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#42. Trapping Rain Water

class Solution:
    # brute force, O(n^2)
    def trap1(self, height: List[int]) -> int:
        N = len(height)
        if N <= 2: return 0

        ret = 0
        for i in range(N):
            max_left, max_right = 0, 0
            # left maximum
            for j in range(i):
                max_left = max(max_left, height[j])
            # right maximum
            for j in range(i+1, N):
                max_right = max(max_right, height[j])

            h = min(max_left, max_right)
            ret += h - height[i] if h > height[i] else 0

        return ret

    # DP
    def trap2(self, height: List[int]) -> int:
        N = len(height)
        if N <= 2: return 0
        
        ret = 0
        lefts, rights = [0]*N, [0]*N
        max_v = 0
        for i in range(N):
            max_v = max(max_v, height[i])
            lefts[i] = max_v
        max_v = 0
        for i in range(N-1, -1, -1):
            max_v = max(max_v, height[i])
            rights[i] = max_v
        for i in range(N):
            h = min(lefts[i], rights[i])
            ret += h - height[i]
            
        return ret

     # Two Pointer
    def trap3(self, height: List[int]) -> int:
        N = len(height)
        if N <= 2: return 0

        ret = 0
        left, right = 0, N-1
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    ret += left_max - height[left]
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    ret += right_max - height[right]
                else:
                    right_max = height[right]
                right -= 1

        return ret





