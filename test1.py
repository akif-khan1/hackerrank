                                   ## hackerrank 5th challenge ##

# n = int(input(""))

# if n > 0:
#     i = list(range(n))
    
# for x in i:
#     print (x*x)



#                                         # 6th challenge ##

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0 and year % 400 == 0:
#             leap = True
#         elif year % 100 != 0 and year % 400 != 0:
#             leap = True
#         else:
#             leap = False
#     else:
#         leap = False
#     return leap

# year = int(input())

# print (is_leap(year))


 
#                                           # 7th challenge ##

#         # solution from hackerrank ##
# N = int(input())
# print(*range(1,N+1), sep='')    # use of xrange function

# print (*range(10,20+1), sep='')

#                                           # 8th challenge ##

       ## this solution is from hackerrank
# import sys
# import re
# p = re.compile(r'(?<=\w)([\$\#\%\s]+)(?=\w)')
# dem = sys.stdin.readline().split();
# r = int(dem[0])
# c = int(dem[1])
# rows = [l for l in sys.stdin]
# text = "";
# for i in range(c):
#     for j in range(r):
#         text = text+rows[j][i]
# print(p.sub(' ',text))


                                        ## rstrip practice ##

# a = ('my, name, is, atif, khan, i, m 35yrs old').rstrip(' imkhdyodrsl35,')
# print (a)          # rstrip is a string method & start removing characters from the last until it found
                     # a character which is not available in strip string.

# n = ['a', 'b', 'c', 'd', 'e', 'f']
# k = int(input(''))

# print (n[0:999:5])

# antiq = ('my name is khan')
# print (antiq[0:999:2])

                                   ## number game practice ##

# n = 84

# guesses = 1

# print ('Number of guesses are limited to 9 times only!')

# while guesses <= 9:
#        n = int(input('enter a number! \n'))
#        if n < 84:
#               print ('your guess is less than winning number! \n')
#        elif n > 84:
#               print ('your guess is greater than winning number! \n')
#        else:
#               print ('$$$ you win $$$')
#               print ('you took',guesses, 'guesses to win! ')
#               break
#        guesses = guesses + 1

# if guesses > 9:
#        print ('G@me OvEr!!!')
       

                                          ### hackerrank 9th challenge ###

# n = []
# n.append(1)
# n.append(2)
# n.append(3)
# n.insert(2,9)
# # n.index(1,0,999)

# print (n.index(1,0,99))




# namee = ['atif', 'ibrahim', 'afaf']
# numee = [1,2,3,4]
# tr = (namee.index('afaf',0,99))
# namee.insert(tr,'kulsoom')
# # namee.sort()
# # namee.sort()
# # namee.reverse()
# print (namee)
# namee.extend(numee)
# # namee.pop(-2)
# # namee.remove(1)
# print (namee.index('atif'))
# print (namee.count('atif'))



# my_list = []

# x = 1

# while (x<11):
#        y = my_list.append(int(input()))
#        if y == 99:
#               break
#        x = x+1

# print (my_list)

                                                 #### list comprehension ###

# ls = []
# for i in range(100):
#        if i%3==0:
#               ls.append(i)
# print (ls)

# print ([i for i in range (100) if i % 3 == 0])    ## above lines of code can be written in one line will give the same output ###

# ls = [i for i in range(100) if i%3==0]
# print (ls)                                        ## this code is also same ##

# dict1 =  {i:f"item {i}" for i in range(1000)}
# dict1 =  {i:f"atif{i}" for i in range(100) if i % 10==0}
# dict2 =  {value:key for key,value in dict1.items()}
# print (dict2)

# import os

# x = (os.listdir(r'D:\Python\2020\hackerrank'))

# print (x)

                                                        ### hackerrank challenge ###

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# list_11 = [[x,y,z] for x in list(range(n)) for y in list(range(n)) for z in list(range(n))]

# x, y, z, n = int(input()), int(input()), int(input()), int(input())
# print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ]) # correct code#

# print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])

# print (list_11)

                                                        
                                                        ### hackerrank challenge runner up finder ###

# i = int(input())
# lis = list(map(int,input().split()))[:i]
# z = max(lis)
# while max(lis) == z:
#     lis.remove(max(lis))

# print (max(lis))

# print (lis)

# a = 'my name is khan'.split()
# a = '    my name is khan    '.split()
# print (a)

# n = int(input())

# if n % 2 ==0 and 2<= n <=5:
#     print ('Not Weird')
# elif n % 2==0 and 6<= n<= 20:
#     print ('Weird')
# elif n%2==0 and n > 20:
#     print ('Not Weird')
# else:
#     print ('Weird')

                                                    ### Nested List ###

# my_list= [['ibrahim','atif'] , ['fehan','asim'] , ['jannat','aisha']]
# print (my_list[0][0])

# for x in my_list:
#     for y in x:
#         print (y)

# my_list = []

# at = 0

# while at<10:
#     x=input('enter name! ')
#     my_list.append(x)
#     at=at+1

# print (my_list)
