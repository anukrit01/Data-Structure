# Find the first occurence of an element from the sorted array and return its index

def find(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high)//2

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid-1] != target:
                return mid
            high = mid - 1


# Target
A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
x = find(A, target)
print(x)