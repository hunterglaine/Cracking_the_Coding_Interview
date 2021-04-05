### 1.1 Is Unique
# Implement a unique algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def has_unique_chars(s):
    """Determines if a given string has all unique characters"""
    # If in ASCII, there are 128 chars
    # If length is greater than 128, return False
    # Turn str into a set, if the len is equal to len of string, return True
    # Otherwise return False

    if len(s) > 128:
        return False
    
    if len(set(s)) == len(s):
        return True

    return False


### 1.2 Check Permutation
# Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(s1, s2):
    """Determines if two give strings are permutations of each other"""

    # Are they the same length? If not return False
    # Sort both strings
    # Loop through the range of their length
    # Check if letters match 
    # If not, return False

    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    return s1 == s2

    # OR 

    # Use a dictionary to count the frequenct of letters in s1
    # Loop through s2, if letter not in dict, return False, if it is, decrement count
    # If count == 0, del key

    # letters = {} # {p: 1, i: 1, n: 1, e: 1}
    # # "pine","eni"
    # for char in s1:
    #     letters[char] = letters.get(char, 0) + 1

    # for char in s2:
    #     if not letters.get(char):
    #         return False
    #     letters[char] = letters.get(char, 0) - 1
    #     if letters[char] == 0:
    #         del letters[char]
    
    # if letters:
    #     return False
    # return True


### 1.3 URLify
# Write a method to replace all spaces in a string with '%20'. YOu may assume that
# the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string

def make_url(s):
    """Replace all internal spaces of string with '%20'"""

    # Strip leading/trailing whitespace from given string

    # use .replace to replace ' ' with '%20'
    # OR
    # Loop through given string and if char is " ", add "%20"

    s = s.strip()
    s = s.replace(" ", "%20")
    return s

    # OR

    # s = s.strip()
    # s_lst = []
    # for char in s:
    #     if char == " ":
    #         s_lst.append("%20")
    #     else:
    #        s_lst.append(char)
    # return "".join(s_lst)


### 1.4 Palindrome Permutation
# Given a string, write a function to check if it is a permutationof a palindrome.

# For something to be a permutation of a palindrome, all letter have to appear
# an even number of times (except 1)

def is_palindrome_perm(s):
    """Returns whether or not a string is a permutaion of a palindrome"""

    # make lowercase
    # Loop through given string 
    # if the char is a letter (ord 97-122, incl.)
    # Add it to dict or incr. count

    # Loop through dict values, count odds
    # if odds are greater than 1, return false

    s = s.lower()
    char_ct = {}
    odds = 0

    for char in s:
        if 122 >= ord(char) >= 97:
            char_ct[char] = char_ct.get(char, 0) + 1
    
    for val in list(char_ct.values()):
        if val % 2 != 0:
            odds += 1
        if odds > 1:
            return False

    return True



