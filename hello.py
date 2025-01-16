 print("hello, world") 
 print("my name is rajnish", "i am 24 year old")
 print(25)
 print (35)
 print(25+35)
 name = "rajnish"
 age = 24
 print("my name is :", name)
 print("my age is :", age)
 age2 = age 
 print(age2)
 #arithmetic operators
 a = 5
 b = 2
 print(a+b)
 print(a-b)
 print(a*b)
 print(a/b)
 print(a%b) #remainder
 print(a**b) #a to the power of b

#logical operators
a = 50
b = 30
print(not False) # prints opposite 
print(not a>=b)
#and operator
val1 = True
val2 = False
print("AND operator:", val1 and val2 ) # requires both value true to print true
print("OR operator:", val1 or val2 ) #or operator
print("OR operator:", a == b or a > b)

#type conversion
a = 2
b = 4.25
c = a+b
print(a+b)
print(type(c))

#type casting
a = 1 
b = int("5")
print(a+b)

# a = 10
# b = 5
# sum = a + b
# print("sum of a + b is", sum)

# #question 1
# a = int(input("enter first number "))
# b = int(input("enter second number "))
# print("sum =", a + b)

# #question 2
# side = float(input("enter square side "))
# print("area = ", side ** 2)

# #question 3
# a = float(input("first value "))
# b = float(input("second value "))
# print("average =", (a+b)/2 )

# #question 4
# a = int(input("first number"))
# b = int(input("second number"))
# print(a>=b)

# #length
# name = input("enter your first name : ")
# print("length =", len(name))
name = "$rajnish $anand$"
print(name.count("$"))

str = "hi i am rajnish anand from india"
print(str.count("i"))

str = "india is located in the southeast asia"
print(str.title())

light = "yellow"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")     

age = 12
if(age >= 18):
    print("can vote")
else:
    print("can not vote")

#grade students based on marks
marks = int(input("enter marks "))
if(marks >= 90): 
    print("grade = A",)
if(marks >= 80 and marks <90):
    print("grade = B",)  


