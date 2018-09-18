###########################################
# Let's Have Some Fun
# File Name: lianjia3.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Sep 18 12:15:12 2018
###########################################
#coding=utf-8
#!/usr/bin/python

def findPair1(a, sumV):
    b = sorted(a)
    l = len(a)
    i = 0
    j = l - 1
    while i<j and i<l and j >= 0:
        s = b[i] + b[j]
        if s == sumV:
            print 'i:%d,j:%d' % (b[i], b[j])
            i += 1
        elif s < sumV:
            i += 1
        else:
            j -= 1

def findPair2(a, sumV):
    dt = {}
    l = len(a)
    for i in range(l):
        t = sumV - a[i]
        b = dt.get(t, [])
        if len(b) > 0:
            for j in b:
                print 'i:%d,j:%d' % (a[i], a[j])
        ls = dt.get(a[i], [])
        ls.append(i)
        dt[a[i]] = ls

if __name__ == '__main__':
    a = [2,1,4,10,-5]
    print a
    print 'findPair1:'
    findPair1(a, 5)
    print 'findPair2:'
    findPair2(a, 5)
    for i in range(5):
        print 'hh'
