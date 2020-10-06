# Python Activtiy
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# Part A. starts_with
# Define a function starts_with(s, char) that takes a string and a character
# and returns true if the string starts with that character and false otherwise.
def starts_with(s, char):
    # YOUR CODE HERE
    #check to see if either parameter is empty
    if len(s) > 0 and char != '':
        if s[0] == char:
            return True
        else:
            return False
    #if only one is empty return false
    elif (len(s) == 0 and char != '') or (len(s) != 0 and char == ''):
        return False
    #if they are both empty return true
    else:
        return True


# Part B. starts_with_vowel
# Define a function starts_with_vowel(s) that takes a string and
# returns true if the string starts with a vowel and false otherwise.
# For our purposes, a consonant is any letter other than A, E, I, O, U)
# Your solution should work for both upper and lower cases
def starts_with_vowel(s):
    # YOUR CODE HERE
    #check to see if the string is empty
    if s == '':
        return False
    else:
        #else the string contains letters and needs to be checked
        num = ord(s[0])
        #A
        if num == 65 or num == 97:
            return True
        #E
        elif num == 69 or num == 101:
            return True
        #I
        elif num == 73 or num == 105:
            return True
        #O
        elif num == 79 or num == 111:
            return True
        #U
        elif num == 85 or num == 117:
            return True
        else:
            return False


# Part C. max_min_sum
# Define a function max_min_sum(arr) that takes an array and returns the sum
# of the largest element and the smallest element of the array.
# For an empty array it should return zero
# For an array with just one element, it should return that element
def max_min_sum(arr):
    # YOUR CODE HERE
    min = 0
    max = 0
    if len(arr) > 0:
        min = arr[0]
        max = arr[0]
        for x in arr:
            if x < min:
                min = x
            if x > max:
                max = x
    if min == max:
        return min
    else:
        return min + max
