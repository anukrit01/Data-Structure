# We have to find a number in array which is closest to given target number
def closest_number(A, target):
    min_diff = float('inf')
    low = 0
    high = len(A) - 1
    closest_val = None

    #the edge cases
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high)//2

        # ensuring we do not go beyond the list
        if mid+1 < len(A):
            min_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid - 1] - target)

        # checking if absolute values are minimum
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_val = A[mid - 1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_val = A[mid + 1]
        
        if target < A[mid]:
            high = mid - 1
        elif target > A[mid]:
            low = mid + 1
        # if the mid itself equals to the target value
        else:
            return A[mid]
    return closest_val


# Testing
A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]
A3 = [4, 4, 5, 6, 6 , 6, 6]

print(closest_number(A1, 11))
print(closest_number(A2, 4))
print(closest_number(A3, 5))