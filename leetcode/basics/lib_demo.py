import collections
import itertools
import heapq

'''
regular python3 lib
'''

# SORT
# sort the index based on the value
A = [7,2,5,4]
B = [2,1,4,3]
C = [1,1,2,2,2,3,3]
D = {'a':3,'b':2,'c':1}
print(sorted(range(len(A)), key=A.__getitem__))
# sort A based on B
print([ x for x,y in sorted(zip(A,B), key=lambda x:x[1])])
# sort key based on value in dict
print(sorted(D.keys(), key=D.get))

# DATA STRUCTURE
# set is HashSet and dict is HashMap

# heap
heapq.heapify(A) # build heap
print(A)
heapq.heappop(A) # pop root
print(A)
dt = collections.Counter(C)
print(heapq.nlargest(2, dt.keys(), key=dt.get))
print(heapq.nsmallest(2, dt.keys(), key=dt.get))

# STRING
c = 'A'
print(c.lower())

# MATH
# infinity
minV = float('-inf')
maxV = float('inf')

# collections
count = collections.Counter(C)
print(count)


# itertools
A = [[1,2],[1,3],[1,4]]
for i,j in itertools.permutations(A, 2):
    print(i, end=',')
    print(j)

# complex(real, imag), {real}: real part, {imag}: imaginary part
a1 = complex(1,1)
print("real:%s, imaginary:%s" % (a1.real, a1.imag))
print("abs:%s" %(abs(a1)))

# scientific notation
print(1e-7)

# other
# map(func, list), run func(ele) for ele in list
points = [[1,2],[2,1],[1,0],[0,1]]
points = set(map(tuple, points))
print(points)
