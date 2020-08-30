# find the lenght of a given string

# Python's way:
name = 'AnukritTiwari'
#print(len(name))

# Iterative method:
def iterative_str_len(input_str):
    str_len = 0
    for i in range(len(input_str)):
        str_len += 1
    return str_len


# Recursive method:
def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])


# Testing
print(iterative_str_len(name))
print(recursive_str_len(name))