## hackerrank 5th challenge ##

# n = int(input(""))

# if n > 0:
#     i = list(range(n))
    
# for x in i:
#     print (x*x)

                                        ## 6th challenge ##

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 100 != 0 and year % 400 != 0:
            leap = True
        else:
            leap = False
    else:
        leap = False
    return leap

year = int(input())

print (is_leap(year))

                                          ## 7th challenge ##

