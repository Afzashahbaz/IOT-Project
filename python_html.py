# -*- coding: utf-8 -*-
"""Python.html

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-e0P0DnDHFy42A0ufZEvk-Cm-rEDnqyB
"""

#SYNTAX
print("My Name is Narmeen")

#COMMENT
print("Hello, World!")

#VARIABLE
x=5              #Global Variable
def my_function():
     y=7         #Local Varibale
     return(x+y)
my_function()

#CASTING
x=int(input("Enter any no."))
y=int(input("Enter any no."))
def my_function():
     return(x+y)
my_function()

#If,Elif and Else Statement
x=int(input("Enter No" ))
if x>=80:
  print("A")
elif x>=50:
  print("B")
else:
  print("Fail")

#If and Else Statement
x=int(input("Enter IQ Level"))
y=float(input("Enter CGPA"))
if x>=100 and y>=3.9:
   print("You are not eligible for this job")
else:
  print("You are not eligible for this job")

#WHILE LOOP
x = 100
while x>=0:
  print(x)
  x=x-1

#FOR LOOP(EVEN)
for i in range (2,100,2):
    print(i)

#FOR LOOP(ODD)
for i in range (1,100,2):
    print(i)