# 4.17 saturday
# Lists

# Build this list [0,0,0] two separate ways.
# Method 1:
list1 = [0, 0, 0]

# Method 2:
list2 = []
list2.append(0)
list2.append(0)
list2.append(0)

# Method 3:
list22 = [0]*3

# Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1, 2, [3, 4, 'hello']]
list3[2][2] = 'goodbye'


# Sort the list below:
list4 = [5, 3, 4, 6, 1]
list4.sort()

# alternatively:
sorted(list4)
