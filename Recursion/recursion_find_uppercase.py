# Find the first occurring uppercase letters if any in a given string.

# Using iterarive method:
def find_upper_ite(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return 'No uppercase character found.'


# Using recusive method:
def find_upper_rec(input_str, i=0):
    if input_str[i].isupper():
        return input_str[i]
    if i == len(input_str) - 1:
        return 'No uppercase character found.'
    return find_upper_rec(input_str, i+1)


# Testing
string1 = 'MyProgram'
string2 = 'myProgram'
string3 = 'myprogram'

print(find_upper_ite(string1))
print(find_upper_rec(string2))
print(find_upper_rec(string3))