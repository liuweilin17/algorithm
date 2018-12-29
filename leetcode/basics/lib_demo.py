import collections
import itertools

'''
regular python3 lib
'''

# SORT
# sort the index based on the value
A = [7,2,5,4]
print(sorted(range(len(A)), key=A.__getitem__))

# DATA STRUCTURE
# set is HashSet and dict is HashMap

# STRING
c = 'A'
print(c.lower())

# MATH
# infinity
minV = float('-inf')
maxV = float('inf')

# collections
A = [1,1,2,2,2]
count = collections.Counter(A)
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