def print_rangoli(size):
    # your code goes here
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    hyp = ['-']
    
    reverse_list = []
    for x in range(0,n):
        # print dots
        reverse_list.append(alphabet[x:n])
        # print
        
    z = list(reversed(reverse_list))
    # mid part
    mid = z[-1]
    mid_string = mid[::-1]+mid[1:]
    mm = ''
    for m in mid_string:
        mm += ('-'+m)
    ln = len(mm[1:])
    
    for a in z:
        aa = a[::-1] + a[1:]
        pp = ''
        for p in aa:
            pp += ('-'+p)
        x = pp[1:].center(ln, "-")
        print(x)    
    for b in reverse_list[1:]:
        bb = b[::-1] + b[1:]
        qq = ''
        for q in bb:
            qq += ('-'+q)
        y = qq[1:].center(ln, "-")
        print(y)
    
    
if __name__ == '__main__':