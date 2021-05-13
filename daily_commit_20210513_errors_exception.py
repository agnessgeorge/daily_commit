#1
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print ("operand not supported")

#2
x = 5
y = 0
 
try :

    z = x/y
    print(z)
except:
    print("Impossible , division by zero")
finally:
    y = input("enter a new non-zero divisor: ")
    z = x/y
    print(z)
    print ("All Done!")

#3
def ask():
    while True:
        try:
            a = int(input("Input an integer: "))
        except:
            print("Looks like you did not enter an integer!")
        else:
            print("Yep that's an integer!")
            break
        
    print("Thank you, your number squared is:  %d"%(a**2))


ask()