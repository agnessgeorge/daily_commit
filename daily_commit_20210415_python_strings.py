# 4.15 thursday
# Strings

# Given the string 'hello' give an index command that returns 'e'
s = 'hello'

# Print out 'e' using indexing
print s[1]

# Reverse the string using slicing, reverse step
print s[::-1]

# Reverse the string without slicing
r = [4, 3, 2, 1, 0]
reversed_s = ""
for i in r:
    j = s[i]
    reversed_s = reversed_s + j
print reversed_s

# Given the string hello, give two methods of producing the letter 'o' using indexing.
# method 1:
print s[-1]

# method 2:
print s[4]
