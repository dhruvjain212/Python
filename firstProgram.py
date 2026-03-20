print("hello world!", "hello python!")
print(9+9 )

name = "Dhruv"
age = 24
skills = '''coding'''


age2 = age

print(name, age, skills)
print(age2)

print(type(name), type(age), type(skills)) 

age = 24
old = False
a = None

print(type(age), type(old), type(a))

a = 2
b = 3
sum = a + b
print(sum)

# This is a single line comment
"""This is a multi-line comment
which can span multiple lines"""


#arithmetic operators
d= 1
e= 2
mysum = d+e
print(mysum)
print(a-b)
print(a*b)
print(a/e)  #division always returns a float
print(a//e) #floor division returns the quotient in integer form
print(a%e) #modulus operator returns the remainder
print(d**e) #exponentiation operator returns a raised to the power of b i.e a^b

#relational operators
x= 50
y= 30
print(x == y) #equal to operator returns True if both operands are equal
print(x != y) #not equal to operator returns True if both operands are not equal
print(x > y) #greater than operator returns True if the left operand is greater than the right operand
print(x < y) #less than operator returns True if the left operand is less than the right operand
print(x >= y) #greater than or equal to operator returns True if the left operand is greater than or equal to the right operand
print(x <= y) #less than or equal to operator returns True if the left operand is less than or equal to the right operand


#logical operators
#in python, we have three logical operators: and, or, and not
a = True
b = False 
print(a and b) #and operator returns True if both operands are True
print(a or b) #or operator returns True if at least one of the operands is True 
print(not a) #not operator returns the opposite of the operand

#type conversion vs type casting
#type conversion is the process of converting one data type to another data type. It can be done implicitly or explicitly.
#type casting is the process of converting one data type to another data type explicitly by using a built-in function.
#implicit type conversion is done by the interpreter automatically when it encounters an expression with mixed data types.
#  For example, if we add an integer and a float, the interpreter will convert the integer to a float before performing the addition.
#in short conversion is done automatically and casting is done manually by the programmer.

a, b= 1,"2"
c= int(b) #casting the string "2" to an integer
sum = a + c
print(sum) #output will be 3 because we have converted the string "2" to an integer before performing the addition.

input("Enter your name: ") #input function is used to take input from the user. It always returns a string.
name = input("Enter your name: ")

#Problem: write a program to input two numbers and print their sum
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num1 = num1 + num2
print("sum =", num1 )

#hello