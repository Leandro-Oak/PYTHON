# -*- coding: utf-8 -*-
"""Basic Python core exercises

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rpVhViwP7ANpJ8ZEzOrP0p8F6JxvMm8K

##FizzBuzz
"""

#The given code solves the FizzBuzz problem and uses the word "Solo" and "Learn" instead of Fizz and Buzz.
#It take a input n and outputs the number from 1 to n
#For each multiple of 3, print "Solo" instead of the number
#For each multiple of 5, prints "Learn" instead of the number.
#For numbers which are multiples of both 3 and 5, outputs "SoloLearn"
#You need to change the code to skip the even numbers, so thta logic only applies to odd numbers in the range.

num =  int(input("Insert the number here:"))

def num1(n):
  for x in range(1,n):
      if x%3 == 0 and x%5 == 0:
        print("SoloLearn")
      elif x%5 == 0:
        print("Learn")
      elif x%3 == 0:
        print("Solo")
      else: 
        if x%2 !=0:
          print(x)

#print(num1(num))

#alternative solution 
n = int(input())

for x in range(1, n+1):
    if x % 2 != 0:
        if x % 3 == 0 and x % 5 == 0:
            print("SoloLearn")
        
        elif x % 3 == 0:
            print("Solo")
        
        elif x % 5 == 0:
            print("Learn")
        else:
            print(x)
    else:
        continue

"""-------------------------------

##Celsius to Fahrenheit
"""

# Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

celsius = int(input("Insert the value, in Celsius, here:"))

def ctf(c):
  x = 9/5*c+32
  return x

fahr = ctf(celsius)
print(fahr)

"""---------------------------

##Character Input
"""

#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

#Extras:

#Add on to the previous program by asking the user for another number and 
#printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""

from datetime import datetime


name = input("Insert your name here:")
age = int(input("Insert your age here:"))
number = int(input("Please add another number:"))

def final(a):
  year = datetime.now().year
  total = (100 - a) + year
  return total

when = final(age)
#print(name + ", The day you will complete 100 is:" + str(when))

number1 = 1
while number1 <= number:
  print("{}, The day you will complete 100 is: {}".format(name,when))
  number1 = number1 + 1

"""------------------------------

##Odd Or Even
"""

#Ask the user for a number. Depending on whether the number is even or odd,
#print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.

number2 = int(input("Insert your number here: "))

def oddeven(x): 
  if x % 2 == 0:
    print("This is a even number!")
    if x % 4 == 0:
      print("And  This number is multiple of 4!")
  elif x % 2 != 0:
    print("This is odd number!")
    

oddeven(number2)

#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#If check divides evenly into num, tell that to the user. If not, print a different appropriate message.



num = int(input("Insert the num number here!"))
check = int(input("Insert the check number here!"))

def divide(x,y):
  if x%y == 0:
    print("The number divide evenly")
  else:
    print("The number doens`t divide evenly")



divide(num, check)

"""-----------------------------

##List Less Than Ten
"""

#Take a list, say for example this one:   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


#Extras:

#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b =  []
for i in a:
  if i < 5:
   b.append(i)

print(b)

#and write a program that prints out all the elements of the list that are less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b =  [x for x in a if x < 5]

print(b)

#Ask the user for a number and return a list that contains only elements
#from the original list a that are smaller than that number given by the user.




def lis(g):
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  num = int(input("Insert your number here: "))
  b = [i for i in a if i < g]
  return b

print(lis(num))

"""-----------

##Divisors
"""

#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#(If you don’t know what a divisor is, it is a number that divides evenly into another number.
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


usernumber = int(input("Insert your number here: "))
divisors = []

for n in range(1, usernumber+1):
  if usernumber % n == 0:
    divisors.append(n)
    
print(divisors)

"""##List Overlap"""

#Take two lists, and write a program that returns a list that contains only the
#elements that are common between the lists (without duplicates).
#Make sure your program works on two lists of different sizes.






a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#Extras:

#1 - Randomly generate two lists to test this
#2 - Write this in one line of Python

4**3







