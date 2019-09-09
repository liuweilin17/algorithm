###########################################
# Let's Have Some Fun
# File Name: 223.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Sep  2 09:14:14 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 223. Rectangle Area

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        two_areas = (C-A)*(D-B) + (G-E)*(H-F)
        x_overlap, y_overlap = 0, 0

        # find overlapping x-line length
        x_arr = [A, C, E, G]
        x_arr.sort()
        x_d1 = abs(A-C) # x-length in rec1
        x_d2 = abs(E-G) # x-length in rec2
        if x_arr[3] - x_arr[0] < x_d1 + x_d2:
            x_overlap = x_arr[2] - x_arr[1]

        # find overlapping y-line length
        y_arr = [B, D, F, H]
        y_arr.sort()
        y_d1 = abs(B-D) # y-length in rec1
        y_d2 = abs(H-F) # y-length in rec2
        if y_arr[3] - y_arr[0] < y_d1 + y_d2:
            y_overlap = y_arr[2] - y_arr[1]

        return  two_areas - x_overlap * y_overlap


