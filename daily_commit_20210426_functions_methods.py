# 4.26 Monday
# Functions and Methods Homework

from math import pi
def vol(rad):
    volume = (4 * pi * (rad**3)) / 3
    print volume
    

# check
print "vol(rad)"
vol(2)


def ran_check(num,low,high):
    if num in  range(low, high):
        print "%d is in the range between %d and %d" %(num,low,high)
    else:
        print "not in range"

# Check
print "\nran_check(num,low,high)"
ran_check(5,2,7)

#to return a boolean

def ran_bool(num,low,high):
    print num in  range(low, high)

print "\nran_bool(num,low,high)"
ran_bool(3,1,10)


def up_low(s):
    upp = 0
    low = 0
    for i in s:
        if i.isupper():
            upp +=1 
        elif i.islower():
            low +=1
        else:
            pass
   
    print "Original String : %s" %s
    print "No. of Upper case characters :  %d" %upp
    print "No. of Lower case Characters :  %d" %low


# check
print "\nup_low(s)"
t = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(t)


def unique_list(lst):
    unique = []
    for j in lst:
        if j not in unique:
            unique.append(j) 
    print unique

print "\nunique_list(lst)"
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])


def multiply(numbers):  
    rslt = 1
    for k in numbers:
        rslt *= k

    print rslt


print "\nmultiply(numbers)"
multiply([1,2,3,-4])


def palindrome(s):
    print s[::1] == s[::-1]


print "\npalindrome(s)"
palindrome('madam')



import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    flag = 0
    for letter in alphabet:
        if letter in str1:
            flag = 1
        else:
            flag = 0
            break
        
    
    print flag == 1


print "\nispangram()"
ispangram("The brown fox jumps over the lazy dog")