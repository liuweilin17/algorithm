###########################################
# Let's Have Some Fun # File Name: insersion_sort.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu May  2 17:24:34 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#InsersionSort
#1. worst case: O(n^2)
#2. best case: O(n)
#3. average case: O(n^2)
#4. in place sort
#5. stable

class InsersionSort:
    def insersion_sort(self, A):
        N = len(A)
        for i in range(1, N):
            key = A[i]
            j = i-1
            while j>=0 and A[j] > key:
                A[j+1] = A[j]
                j -= 1
            A[j+1] = key

def showInsersionSort(A):
    s = InsersionSort()
    print(A)
    s.insersion_sort(A)
    print(A)

if __name__ == '__main__':
    print('-------case 1---------')
    A = [2, 3, 1, 4]
    showInsersionSort(A)
    print('-------case 2---------')
    A = []
    showInsersionSort(A)
    print('-------case 3---------')
    A = [1]
    showInsersionSort(A)
    print('-------case 4---------')
    A = [1,2,1]
    showInsersionSort(A)
