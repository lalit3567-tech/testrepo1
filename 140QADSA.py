# Q.1. write a python program to print Hello program
# print("Hello")

# Q.2 Write a Python program to do arithmetical operations addition and division.

#n1 = float(input("enter the no : "))
#n2 = float(input("enter the no : "))
#sum_result = n1 + n2
#print(f"sum:{n1} + {n2} = {sum_result}")

# n3 = float(input("enter the dividend for division : "))
# n4 = float(input("enter divisor for division f: "))
#
# if n4 == 0:
#     print("error infinite no")
# else :
#     division = n3 / n4
#     print(f"division : {n3} / {n4} = {division}")

# Q.3 Write a python program to find the area of triangle
# input the base and height from the user
# base = float(input("Enter the length of the base of the triangle : "))
# height = float(input("Enter the length of the height of the traingle : "))
# # calculate the area of traingle
# area = 0.5 * base * height
# display the result
# print(f"the area of triangle is : {area}")

# Q.4 Write a python program to swap two variables
# Input the variables
# a = 10
# b = 20
# temp = a
# a=b
# b=temp
# print(a,b)

# Q.5 write a python program to generate random number
# import random
# print(f"random number : {random.randint(1,100)}")
# print(random.randint(1,50))

# Q.6 write a python program to convert kilometers into miles
# Miles (mi) are commonly used for distance in countries like the USA and UK,
# # while kilometers (km) are commonly used in India.
# 1 kilometer (km) = 0.621371 miles (mi)
# 1 mile = 1.60934 kilometers

# kilometer = 100
# # f = 0.621371
# # miles = kilometer * f
# # print(f"{kilometer} kilometer is equal to {miles}")

# Q.7 Write a Python program to convert Celsius to Fahrenheit
# Celsius is commonly used in India and most countries.
# Fahrenheit is commonly used in the USA.
# c=25
# f = (c*9/5)+32
# print(f"{f}")

# Q.8 Write a python program to display calender.
# import calendar
# year = int(input("enter the year : "))
# month = int(input("enter the month : "))
# cal = calendar.month(year,month)
# print(cal)

# Q.9 write a python program to solve quadratic equation

# Q. 10 write a python program to swap two variables without temporary variable

# a = 5
# b = 10
# a, b = b,a
# print(a,b)
#
# temp = a
# a = b
# b = temp
# print(a,b)

# Q.10 write a python program to check if a number is positive, negative or zero

# n = float(input("enter the number : "))
# if n == 0:
#     print("no is zero")
# elif n > 0:
#     print("no is positive")
# else :
#     print("no is negative")

# Q.11 write a python program to check if no is even or odd.
# n = 4
# if n%2 == 0 :
#     print("the no is even")
# else :
#     print("the no is odd")

# Q.12 write a python to program to check leap year
# A leap year is a year that has 366 days instead of 365 days.
# The extra day is added to February, so February has 29 days instead of 28.
# It is divisible by 4 and 400 , not a divisible by 100

# year = int(input("enter the year"))
# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is leap year".format(year))
# elif (year % 4 == 0) and (year % 100 !=0):
#     print("{0} is leap year.format(year)")
# else :
#     print("{0} is not a leap year".format(year))

# y = 2026
# if (y%400 == 0) and (y%100 == 0):
#     print("leap year")
# elif (y%4 == 0) and (y%100 !=0) :
#     print("leap year")
# else :
#     print("Is not leap year")

# Q.13 write a python program to check prime number
# the no is divide by itself and 1
# p = 2
# count = 0
# if (p == 0) or (p == 1):
#     print("the no is not prime")
# elif (p>0) and (p>1):
#     for i in range(1, p + 1):
#         if (p % i == 0):
#             count += 1
#
#     if (count == 2):
#         print("the no is prime")
#     else:
#         print("the no is not prime")
#
# p = 13
# flag = False
# if (p == 0 ) or (p == 1) :
#     print("no is not prime")
# elif (p>0) and (p>1) :
#     for i in range(2,p):
#         if (p%i)==0:
#             flag = True
#             break
#     if flag:
#         print("no is not prime")
#     else :
#         print("no is prime")

# Q.14 write a python program to print all prime numbers in an interval of 1-10

# lower = 1
# upper = 10
# for num in range (lower,upper+1):
#     if num > 1:
#         for i in range (2,num):
#             if (num % i) == 0:
#                 break
#         else :
#             print(num)

# Q.15 Write a python program to find factorial number

# n1 = int(input("enter the number : "))
# fact = 1
# for i in range (1,n1+1):
#     fact = fact * i
# print(fact)

# Q.16 write a python program to display the multiplication table
# n = 10
# for i in range (1,10):
#     print(f"{n} * {i} : {n*i}")

# Q.17 Write a python program to print the fibonacci numbers
# fibonacci series is a series of numbers where each number is sum of two preceding numbers.

# n = int(input("enter the number : "))
# n1, n2 = 0,1
# count = 0
# if n<=0 :
#     print("please enter positive number")
# elif n ==1 :
#     print("enter fibonnaci upto n")
#     print(n1)
# else :
#     print("Fibonacci sequence")
#     while count < n:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count +=1

# Q. find the given no is armstrong or not
#
# n = int(input("enter the number : "))
# num = n
# sum = 0
#
# while n > 0:
#     dig = n % 10
#     sum = sum + dig * dig * dig
#     n = n // 10
# print(sum)
# if sum == num :
#     print("armstrong number")
# else:
#     print("not a armstrong number")

# Q.18. find the armstrong number in the given range
#
# for num in range(150, 500):
#
#     n = num
#     sum = 0
#
#     while n > 0:
#         dig = n % 10
#         sum = sum + dig * dig * dig
#         n = n // 10
#
#     if sum == num:
#         print(num)

# Q.19. find the sum of n natural number
#
# limit = int(input("enter the number : "))
# sum = 0
# for i in range(1,limit+1):
#     sum += i
# print(sum)

# Q.20. write a python program to find sum of elements of array

#my_list = [1, 2, 3, 4, 5,6]

# # arr_sum = sum(my_list)
# # print(arr_sum)
# def sum_of_array(arr):
#     sum = 0
#     for i in arr:
#         sum = sum + i
#     return sum
#
# print(sum_of_array([1, 2, 3, 4, 5,6]))









