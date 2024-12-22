# print("hello,world!")
# print(25)
# print(24+24)

# name = "raj"
# age = 24
# print('my name is',name, "i am",age, "years old")

# age2 = age 
# print(age2)


# a = 20
# b = 30
# print(not False)
# print(not a<=b)


# val1  = True
# val2 =  False
# print("or operator:",val1 or val2)


# a = 2
# b = 4.25
# c = a + b
# print(type(c),c)

# a = 1 
# b =int("5")
# print((type),a+b)
# print(type(a+b))

# a = int(input("first value ")) # int is used to take input in integer
# b = int(input("sencond value "))
# average = (a+b)/2
# print("average is:", average)
# print(type(average), "average is:", average )


# a = int(input("first number"))
# b = int(input("second number"))
# print(a>=b)

# name = input("enter your name ",)
# print("length is:", len(name))

# print(name.count("a"))

# str = 'india is located in the south east asia'
# print(str.title())

# light = "green"
# if light == "red":
#     print("stop")
# elif light == "green": # use elif if 'if' is not applicable
#     print("go")
# elif light == "yellow":
#     print("look")
# else:
#     print("light is broken")

# age = 22
# if age>=18:
#     print("can vote")
# else:
#     print("cannot vote")


# marks = int(input("enter marks "))
# if marks >= 90:
#     print("grade = A")
# if marks >= 80 and marks < 90:
#     print("grade = B")
# else:
#     print('passed')

# num = 100
# num -= 20
# print(num)

# num = 100
# num = 80
# num = num+num
# print(num)

# is_raining = False
# if not is_raining:
#     print("let's go for a walk")
# else:
#     print("stay home")

# is_raining = True
# if is_raining == False:
#     print("let's go for a walk")
# else:
#     print("stay home")

# age  = int(input("enter your age "))
# age+=10
# print("age in 10 years will be:", age)

# high_school = input("high school pass or not (yes/no): ").strip().lower()
# age = int(input("enter age "))
# if high_school == "yes" and age > 17:
#     print("eligible")
# else:
#     print("not eligible")
 
# age = int(input("enter your age "))
# if age <=12:
#     print("you are kid and kids are eligible for special discount")
# elif age <= 20: 
#     print("You are a student and available for discount")
# elif 21 <= age < 30:
#     print("you are under young adults special discounts may apply")
# elif 30 <= age < 60:
#     print("regulars customers may have exclusive offers. please inquire!")
# elif age >= 60:
#     print("you are senior citizen and you are eligible for discount")

# else:
#     print("sorry, No Discount available")



# high_school = input("high school pass or not (yes/no): ").strip().lower() == "yes"
# age = int(input("enter age "))
# if high_school and age > 17:
#     print("eligible")
# else:
#     print("not eligible")

# name = "rajnish"
# length = len(name)
# middle_index = length//2
# print("middle character is:", name[middle_index])

# name = "rajnish anand"
# print(name[0:13:4])

# text= "python programming"
# print(text[0:16:2])

# fruits = {"mango": 10,
#           "pineapple": 5,
#           "guava": 20,
#           }
# print(fruits["guava"])


# count = 100
# while count >=1:
#     print(count)
#     count-=1

# i= 1
# n = 9
# while i <=10:
#     print(n*i)
#     i+=1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(nums):
#     print(i)
#     i+=1



# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i<len(nums):
#     print(nums[i])
#     i+=1


# def fact(n):
#     if n == 0:
#         return 1
#     return fact(n-1)*n

# print(fact(5))


# def square(b,p):
#     if p == 0:
#         return 1
#     return square(b,p-1)*b

# print(square(5,2))


# a = int(input("enter number "))
# b = int(input("enter number "))
# product = a*b
# print(product)

# def product(a,b):
#     return a*b

# print(product(5,9))

def add(a,b):
    return a+b
def product(a,b):
    return a*b
def subtract(a,b):
    return a-b
def divide(a,b):
    # Handles diviosn by zero
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a/b

def ask_user():

    ''' In Python, a variable created inside a function, 
    like a and b in ask_user(), is called a local variable. 
    This means that a and b exist only within the 
    ask_user() function.'''
   
    a = float(input("Enter first number "))
    b = float(input("Enter second nuber "))
    operator =input("Choose operation (+,-,*,/)")
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = subtract(a, b)
    elif operator == '*':
        result = product(a, b)
    elif operator == '/':
        result = divide(a, b)
    else:
        # If the operator is not valid, set an error message
        result = "Error: Invalid operator."

        # Step 3: Display the result
    print("Result:", result)

ask_user()  












