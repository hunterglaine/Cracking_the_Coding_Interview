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


### 1.5 One Away
# There are three types of edits that can be performed on strings: insert a 
# character, remove a character, or replace a character. Given two strings,
# write a function to check if they are one edit (or zero edits) away.

# Checking to see if the two strings are the same or only one edit away

def one_away(s1, s2):
    """Return whether two strings are the same or only one edit away"""
    # If the two strings are the same, return True
    if s1 == s2:
        return True

    # If one is longer, go through that string and put it in dict with freq ctr
    # Loop through the second string, look to see if the letter is in the dict
    # If not, up diff_ctr by 1
    # If so, decrement the ctr
    # If it's 0, remove the key
    # After that loop, if the dict still exists, if only one letter and they're 

    dic = {}
    diff_ctr = 0

    for char in s1:
        dic[char] = dic.get(char, 0) + 1
    
    for char2 in s2:
        dic[char2] = dic.get(char2, 0) - 1
        if dic[char2] <= 0:
            if dic[char2] == -1:
                diff_ctr += 1
            del dic[char2]
    
    if len(dic) == 1 and (diff_ctr == 1 or diff_ctr == 0):
        return True
    if len(dic) > 1:
        return False
    
    if diff_ctr <= 1:
        return True
    return False


### 1.6 String Compression
# Basic string compression - "aabcccccaaa" -> "a2b1c5a3"

def compress_string(s):
# Create a variable to find out if dups touching, set to False
# If False at the end, return original string, otherwise, newly created string
# Create a new empty string, comp
# ctr = 1
# Loop through given string, s, in range length minus 1
# if curr is equal to next, incr ctr by 1
# if not, add curr to empty string, plus ctr
# set ctr to 1

    dups = False # T
    comp = "" # "a2b1"
    ctr = 1 # 3
    # aabccc"

    for i in range(len(s)-1): # 4 - 4
        if s[i] == s[i+1]: # 
            ctr += 1
            if ctr >= 2:
                dups = True
        else:
            comp += f"{s[i]}{ctr}"
            ctr = 1
    if ctr > 1:
        comp += f"{s[-1]}{ctr}"

    if dups:
        return comp
    return s


### 1.7 Rotate Matrix
# Given an N x N matrix, rotate in place by 90 degrees.
# [1,2][3,4]
def rotate_matrix(matrix):
    
    n = len(matrix[0]) # 2

    for x in range(n//2 + n%2): # 0
        for y in range(n//2): 
            tmp = matrix[n-y-1][x]
            matrix[n-y-1][x] = matrix[n-x-1][n-y-1]
            matrix[n-x-1][n-y-1] = matrix[y][n-x-1]
            matrix[y][n-x-1] = matrix[x][y]
            matrix[x][y] = tmp
    return matrix


### 1.8 Zero Matrix
# Write an algortihm such that if an element in an M x N matrix is 0, its entire row
# and column are set to 0

def turn_to_zeros(matrix):
    """Turn given m x n matrix row and column to 0 if zero exists"""

    # Loop through horizontally
    # Loop through vertically
    # If element equals 0, 
    # Add its x to a set
    # Add its y to a set
    x_set = set()
    y_set = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])): 
            if matrix[i][j] == 0:
                x_set.add(i)
                y_set.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in x_set and matrix[i][j] != 0:
                matrix[i][j] = 0
            if j in y_set and matrix[i][j] != 0:
                matrix[i][j] = 0


### 1.9 String Rotation
# You have a method, isSubstring to check if one word is a substring of another. 
# Given two string, s1 and s2, write code to check if s2 is a rotation of s1 using 
# only on call to isSubstring.
def isSubstring(string_1, string_2):
    pass

def is_rotated(s1,s2):
    if len(s1) == len(s2) and len(s1) > 0:
        s1s1 = s1 + s1
        return isSubstring(s1s1,s2)
    return False
