#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    # Return the first 5 characters of the given string
    return s[:5]

def last_seven(s):
    # Return the last 7 characters of the given string
    return s[-7:]

def middle_number(n):
    # Convert number to string and return the second and third characters
    s = str(n)
    return s[1:3]

def first_three_last_three(s1, s2):
    # Return the first 3 of s1 and last 3 of s2 combined
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
