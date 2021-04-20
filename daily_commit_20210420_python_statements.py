# Statement assessment test
# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for x in st.split():
    if x.startswith('s'):
        print x


# create this ['Print only the word', ' that ', 'tart with ', ' in thi', ' ', 'entence']
st2 = st.split('s')
print st2


# Use range() to print all the even numbers from 0 to 10.
for a in range(0, 11):
    if a % 2 == 0:
        print a

print [b for b in range(0, 10) if b % 2 == 0]


# List Comprehension
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print [c for c in range(1, 51) if c % 3 == 0]


# Go through the string below and if the length of a word is even print "even!"
st3 = 'Print every word in this sentence that has an even number of letters'
for f in st3.split():
    if len(f) % 2 == 0:
        print f + " has even length!"

# Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
for d in range(1, 101):
    if d % 3 == 0 and d % 5 == 0:
        print "FizzBuzz"
    elif d % 3 == 0:
        print "Fizz"
    elif d % 5 == 0:
        print "Buzz"
    else:
        print d


# Use List Comprehension to create a list of the first letters of every word in the string below:
st4 = 'Create a list of the first letters of every word in this string'
print [e[0] for e in st4.split()]
