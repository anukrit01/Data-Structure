'''
an array that starts off with increasing terms and then concludes
with decreasing terms. In any such sequence, there is a “peak” element
which is the largest element in the sequence.
NOTE: A bitonic sequence is a sequence of integers
      such that: x0<...<xk>...>xn−1x_0 < ... < x_k > ... > x_{n-1}x​0​​<...<x​k​​>...>x​n−1​​ 
      for some k, 0 <= k < n
For Ex.: 1, 2, 3, 4, 5, 4, 3, 2, 1
'''

def highest_peak(A):
    low = 0
    high = len(A) - 1
    
    if len(A) < 3:
        return None
    
    while low <= high:
        mid = (low + high)//2

        mid_left = A[mid - 1] if mid - 1 > 0 else float('-inf')
        mid_right = A[mid + 1] if mid + 1 < len(A) else float('inf')

        if A[mid_left] < A[mid] and A[mid_right] > A[mid]:
            low = mid + 1
        elif A[mid_left] > A[mid] and A[mid_right] < A[mid]:
            high = mid - 1
        elif A[mid_left] < A[mid] and A[mid_right] < A[mid]:
            return A[mid]
    return None


# Testing
A1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
A2 = [1, 6, 3, 2, 0]
A3 = [5, 8, 3, 3, 5]

print(highest_peak(A1))
print(highest_peak(A2))
print(highest_peak(A3))