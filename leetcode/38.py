###########################################
# Let's Have Some Fun
# File Name: 38.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Nov 15 13:31:47 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 38. Count and Say

ass Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in range(n-1):
            pre = '' # 前一个字符
            cur = '' # 第i个字符串
            num = 0 # 字符串中每个字符的个数
            for c in s:
                if pre == '' or c == pre:
                   num += 1
                else:
                    cur += str(num) + pre
                    num = 1
                pre = c
            cur += str(num) + c # notice！！！
            s = cur
        return s

if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(1))
    print(s.countAndSay(5))

