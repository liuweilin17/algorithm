###########################################
# Let's Have Some Fun
# File Name: 1109.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun  7 Jul 11:33:31 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1109. Corporate Flight Bookings

class Solution:
    # given i, j, k
    # every node between [i-1, ..., j-1] is added with k
    # every node after j-1 minus with k
    # then we could incremently add every value in ret to get the final result
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ret = [0] * (n+1) # n+1 instead of n, because we need to minus k after j
        for i, j, k in bookings:
            ret[i-1] += k
            ret[j] -= k

        for i in range(n):
            ret[i+1] += ret[i]

        return ret[:-1]


