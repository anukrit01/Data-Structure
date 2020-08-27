# Find the first occurence of an element from the sorted array and return its index
# using Python's Bisect method
# NOTE:  Bisect is a built-in binary search method in Python.
#       It can be used to search for an element in a sorted list.

import bisect

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

# The bisect_left function finds the index of the target element.
# In the event where duplicate entries are satisfying the target element,
# the bisect_left function returns the left-most occurrence.
print(bisect.bisect_left(A, -10))
print(bisect.bisect_left(A, 108))

# The bisect_right function returns the insertion point which comes after,
# or to the right of, any existing entries of the target element in the list.
print(bisect.bisect_right(A, -10))
print(bisect.bisect_right(A, 401))

# bisect works same as bisect_right
print(bisect.bisect(A, -10))

# the insort functions insert at the index positions.
print(A)
bisect.insort_left(A, 0)
print(A)

print(A)
bisect.insort_right(A, 300)
print(A)
