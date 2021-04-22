# 4.22 Thursday
# Python Quiz on Functions

print "lesser_of_two_evens()"
def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 == 0:
        print min(a,b)
    else:
        print max(a,b)

# Check
lesser_of_two_evens(2,4)
lesser_of_two_evens(5,20)


print " "
print "animal_crackers()" 
def animal_crackers(c):
    first_letters = []
    for animal in c.split():
        first_letters.append(animal[0])
    
    if first_letters[0] == first_letters[1]:
        print True
    else:
        print False

# Check
animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')


print " "
print "makes_twenty()"
def makes_twenty(e,f):
    if e == 20 or f == 20 or e + f ==20:
        print True
    else:
        print False


# Check
makes_twenty(20,10)
makes_twenty(12,8)
makes_twenty(2,3)

print " "
print "old_macdonald()"
def old_macdonald(h):
    g = list(h)
    g[0] = g[0].upper()
    g[3] = g[3].upper()
    
    print ''.join(g)


# Check
old_macdonald('macdonald')
old_macdonald('wangugugu')


print " "
print "master_yoda()"
def master_yoda(j):
    k = j.split()
    l = k[::-1]
    print " ".join(l)

# Check
master_yoda('I am home')
master_yoda('We are ready')


print " "
print "almost_there()"
def almost_there(m):
    if abs(m - 100) <= 10 or abs(m - 200) <= 10:
        print True
    else:
        print False

# Check
almost_there(90) 
almost_there(104)
almost_there(150)
almost_there(209)


print " "
print "has_33()"
def has_33(n):
    strng = ""
    for o in n:
        strng = strng + str(o)
    


    if '33' in strng:
        print True
    else:
        print False

# Check
has_33([1, 3, 3]) 
has_33([1, 3, 1, 3]) 
has_33([3, 1, 3])


print " "
print "paper_doll()"
def paper_doll(p):

    r = ""

    for q in p:
        r = r + (q*3)
   
    print r

#Check
paper_doll('Hello')
paper_doll('Mississippi')


print " "
print 'blackjack()'
def blackjack(s,t,u):
    v = s + t + u
    if v <= 21:
        print v
    elif v <= 31 and (s == 11 or t == 11 or u == 11):
        v -= 10 
        print v  
    else:
        print "BUST"


#Check
blackjack(5,6,7)
blackjack(19,9,9)
blackjack(9,9,11)
