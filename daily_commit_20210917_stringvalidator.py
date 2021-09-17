if __name__ == '__main__':
    s = raw_input()
#     In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
    print(any([str.isalnum(x) for x in s]))
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
    print(any([str.isalpha(x) for x in s]))
# In the third line, print True if  has any digits. Otherwise, print False.
    print(any([str.isdigit(x) for x in s]))
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
    print(any([str.islower(x) for x in s]))
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
    print(any([str.isupper(x) for x in s]))
