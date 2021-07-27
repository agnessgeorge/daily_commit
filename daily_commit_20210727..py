def swap_case(s):
    u = ""
    for t in s:
        if t.isupper() == True :
            u += t.lower()
        elif t.islower() == True:
            u += t.upper()
        else:
            u += t
    return u


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)