# calculate the product of given two integers using recursion.
# NOTE: Do not use '*' anywhere.

def recursive_product(x, y):
    # This cuts down on the total number of
    # recursive calls:
    if x < y:
        return recursive_product(y, x)
    if y == 0:
        return 0
    return x + recursive_product(x, y-1)


# Testing
print(recursive_product(500, 2000))
print(recursive_product(2, 12))