###########################################
# Let's Have Some Fun
# File Name: 658.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Mar  2 23:22:17 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#658. Find K Closest Elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        low, high = 0, N-1
        while low <= high:
            mid = (high - low) // 2 + low
            if arr[mid] > x:
                high = mid - 1
            elif arr[mid] < x:
                low = mid + 1
            else:
                low = mid
                break

        # use two pointer
        i, j = low-1, low
        step = k
        while step > 0 and i>=0 and j<N:
            if x - arr[i] <= arr[j] - x:
                i -= 1
            else:
                j += 1
            step -= 1

        if i < 0:
            j += step
        elif j >= N:
            i -= step
        return arr[i+1:j] # i+1 and j-1 is valid.


