# 4.24 saturday
# functions 2


def summer_69(arr):
    total = 0
    if 6 not in arr:
        for x in arr:
            total += x   
    else:
        for x in arr:
            if arr.index(x) < arr.index(6) or arr.index(x) > arr.index(9):
                total += x
    print total

# check
print "summer_69()"
summer_69([1,3,5])
summer_69([4,5,6,7,8,9])
summer_69([2, 1, 6, 9, 11])


def spy_game(lst):
    lst2 = ""
    if 0 not in lst:
        print "no zero in this list"
    else:
        for item in lst:
            if item == 0 or item == 7:
                lst2 += str(item)
            else:
                pass
        if '007' in lst2:
            print True
        else:
            print False
    

        
print " "
print "spy_game()"
spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])



def count_primes(num):
    count = 0
    for y in range(2,num+1):
        factors = 0
        for z in range(1,y+1):  
            if y % z == 0:
                factors += 1
            else:
                pass  
        if factors > 2:
            pass
        else:
            count += 1
    print count


print " "
print "count_primes()"
# check
count_primes(100)


def print_big(ltr):
    d = {
    'a':'  *  \n * * \n*****\n*   *\n*   *',
    'b':'**** \n*   *\n**** \n*   *\n**** ',
    'c':'  * *\n *   \n*    \n *   \n  * *',
    'd':'* *  \n*   *\n*   *\n*   *\n* *  ',
    'e':'* * *\n*    \n* * *\n*    \n* * *'
    }
    print d[ltr]

print " "
print "print_big()"
# check
print_big('a')
print_big('b')
print_big('c')
print_big('d')
print_big('e')