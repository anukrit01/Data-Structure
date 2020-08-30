# Given a string, count the number of consonants present in it.

vowels = 'AEIOUaeiou'

# Iterative method:
def iterative_count(input_str):
    consonents = 0
    for i in range(len(input_str)):
        if input_str[i] not in vowels and input_str[i].isalpha():
            consonents += 1
    return consonents


# Recursive method:
def recursive_count(input_str):
    if input_str == '':
        return 0
    
    if input_str[0] not in vowels and input_str[0].isalpha():
        return 1 + recursive_count(input_str[1:])
    else:
        return recursive_count(input_str[1:])


# Testing
name = 'Anukrittiwari01'
print(iterative_count(name))
print(recursive_count(name))