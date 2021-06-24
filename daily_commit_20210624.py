def is_leap(year):
    leap = False
    
    if (1900 <= year <= 100000):

        if year%400 == 0:
            leap = True
            print(leap)
        elif year%4 == 0 and year%100 != 0:
            leap = True
            print(leap)
        else:
            # year is not leap
            print(leap)
            
    else:    
        print("year out of range") 
        call_func()
    

def call_func():
    year = int(input())
    is_leap(year)


call_func()