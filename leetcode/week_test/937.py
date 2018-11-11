###########################################
# Let's Have Some Fun
# File Name: 937.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 11 13:10:49 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 937. Reorder Log Files

import functools

class Solution(object):
    def cmp(self, a, b):
        a_arr = a.split(' ', 1)
        b_arr = b.split(' ', 1)
        if a_arr[1][0] >= '0' and a_arr[1][0] <= '9':
            if b_arr[1][0] >= '0' and b_arr[1][0] <= '9':
                # a < b
                return 0 # 不动
            else:
                # a > b
                return 1 # 动
        else:
            if b_arr[1][0] >= '0' and b_arr[1][0] <= '9':
                # a < b
                return -1 # 不动
            else:
                if a_arr[1] == b_arr[1]:
                    return 1 if a_arr[0] > b_arr[0] else -1
                else:
                    return 1 if a_arr[1] > b_arr[1] else -1

    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        l = len(logs)
        if l <=1:
            return logs

        return sorted(logs, key=functools.cmp_to_key(self.cmp))


if __name__ == '__main__':
    s = Solution()
    input = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print(input)
    print(s.reorderLogFiles(input))
