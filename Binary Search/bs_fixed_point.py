'''
Given an array of nnn distinct integers sorted in ascending order,
write a function that returns a fixed point in the array. If there
is not a fixed point, return None.
NOTE: A fixed point in an array A is an index i such that A[i] is equal to i.
'''

# Method-1: Linear Search
# TC: O(n)
#SC: O(1)
def fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None


# Method-1: Binary Search
# TC: O(log n)
#SC: O(1)
def fixed_point_binary(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high)//2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None


# Testing
A = [2, 2, 3, 5, 5, 37, 54]
print(fixed_point_binary(A))