###########################################
# Let's Have Some Fun
# File Name: quick_sort.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct  5 19:52:38 2018
###########################################
#coding=utf-8
#!/usr/bin/python

import random

class QuickSort:
    def swap(self, A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp

    def partition1(self, A, p, r):
        i = p-1
        pivot = A[r]
        for j in range(p, r):
            if A[j] <= pivot:
                i += 1
                self.swap(A, i, j)
        self.swap(A, i+1, r)
        return i+1

    # HOARE-PARTITION, the original version
    def partition2(self, A, p, r):
        pivot = A[p]
        i = p - 1
        j = r + 1
        while(True):
            condition = True
            while condition:
                j -= 1
                if A[j] <= pivot:
                    break
            while condition:
                i += 1
                if A[i] >= pivot:
                    break
            if i < j:
                self.swap(A, i, j)
            else:
                return j

    def randomizedPartition(self, A, p, r):
        i = random.randint(p, r)
        self.swap(A, i, r)
        return self.partition1(A, p, r)

    def quick_sort(self, A, p, r):
        if p < r:
            #q = self.partition1(A, p, r)
            #q = self.partition2(A, p, r)
            q = self.randomizedPartition(A, p, r)
            self.quick_sort(A, p, q-1)
            self.quick_sort(A, q+1, r)

    def sort(self, A):
        self.quick_sort(A, 0, len(A)-1)

def showQuickSort(A):
    s = QuickSort()
    print A
    s.sort(A)
    print A

if __name__ == '__main__':
    s = QuickSort()
    print '-------case 1---------'
    A = [2, 3, 1, 4]
    showQuickSort(A)
    print '-------case 2---------'
    A = []
    showQuickSort(A)
    print '-------case 3---------'
    A = [1]
    showQuickSort(A)
    print '-------case 4---------'
    A = [1,2,1]
    showQuickSort(A)

