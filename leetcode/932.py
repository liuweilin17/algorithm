###########################################
# Let's Have Some Fun
# File Name: 932.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed  3 Jul 21:24:52 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#932. Beautiful Array

class Solution:
    # 1. if A is an odd and beautiful array, B is an even and beautiful array, then A+B is an beautiful array
    # 2. if A is a beautiful array, deleting from A could still remain beautiful
    # 3. if A is a beautiful array, add a to A's each element could still remain beautiful
    # 4. if A is a beautiful array, multiply a to A's each element, could still remain beautiful
    # Therefore
    # given beautiful array A of N
    # 2 * A - 1 is odd number of beautiful array of 2N
    # 2 * A is even number of beautiful array of 2N
    # Therefore, the beautiful array of 2N is (2*A - 1) + (2*A)
    def beautifulArray(self, N: int) -> List[int]:
        ret = [1]
        while len(ret) < N:
            ret = [2*i-1 for i in ret] + [2*i for i in ret]
        return [i for i in ret if i <= N]


