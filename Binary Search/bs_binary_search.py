# First go through the linear search in python
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


# Binary Search (iterative method):
def binary_search_iterative(data, target):
    low = 0 
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# Binary Search (recursive method):
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high)//2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)


# Testing
data = [1, 3, 5, 9, 78, 55, 12]
print(linear_search(data, 12))
print(linear_search(data, 15))

arr = [23, 25, 66, 78, 81, 301, 654]
print(binary_search_iterative(arr, 654))
print(binary_search_iterative(arr, 56))

print(binary_search_recursive(arr, 81, 0, len(arr)-1))
print(binary_search_recursive(arr, 524, 0, len(arr)-1))