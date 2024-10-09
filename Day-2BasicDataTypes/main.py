# Integer Operations
num1 = 45
num2 = 3
print("Operations using Integers")
print(f"{num1} + {num2} is {num1+num2} ")
print(f"{num1} - {num2} is {num1-num2} ")
print(f"{num1} * {num2} is {num1*num2}" )
print(f"{num1} /{num2} is {num1/num2} ")
print(f"{num1} % {num2} is {num1%num2} ")
print("-------------------------------")
# Floating Point Operations
float1 = 22.35
float2 = 9.3
print("Operations using Floating point numbers")
print(f"{float1} + {float2} is {float1+float2} ")
print(f"{float1} - {float2} is {float1-float2} ")
print(f"{float1} * {float2} is {float1*float2}" )
print(f"{float1} /{float2} is {float1/float2} ")
print(f"{float1} % {float2} is {float1%float2} ")
print("-------------------------------")
# String Concatenation
print("Concatenation of Strings")
str1 = "Hi! I love python "
str2 = "I'\m also learning GenAI"
print(f"String after concatenating {str1} and {str2} is : {str1+str2}")
print("-------------------------------")
# Boolean Logic
print("Understanding Boolean Logic")
has_python_knowledge = True
has_django_knowledge = False
print(f"Has knowledge on Python? {has_python_knowledge}")
print(f"Has knowledge on Django? {has_django_knowledge}")
print(f"Can you create the webApps using Python and Django? {has_python_knowledge and has_django_knowledge}")
print("-------------------------------")
# User Input
print("Accepting input from User in below ways:")
# Normal input()
print("Enter username:")
user = input()
print("Enter your age:")
age = int(input())  #converting from string to int

exp = float(input("Enter your Experience:(only number)"))

print("Your entered values are: ")
print("{0:30}{1:10}{2:10}".format("UserName","Age","Experience"))
print("{0:30}{1:10}{2:10}".format(user,age,exp))
print("------------------------------")
# Control structures - If -Else
print("Enter three values seperated by just comma")
a,b,c=map(int,input().split(','))
if(a>b and a>c):
    print(f"{a} is greater than {b} and {c}")
elif (b>a and b>c):
    print(f"{b} is greater than {a} and {c}")
else:
    print(f"{c} is greater than {a} and {b}")


