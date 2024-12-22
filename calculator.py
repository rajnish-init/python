# a = float(input("Enter first nummber ")) #used floats beacause it will accept both 'int' and 'floats' 
# b = float(input("Enter second number "))
# operator = input("Enter an operation (+,-,*,/): ")
# if operator == '+':
#     result = a + b
# elif operator == '-':
#     result = a - b
# elif operator == '*':
#     result = a * b
# elif operator == '/':
#     if b == 0:
#         result = "Error: Division by zero is not allowed."
#     else:
#         result = a/b
# else:
#     result = "Error: Invalid operator."

# print("Result:", result)


# def add(a,b):
#     return a+b
# def product(a,b):
#     return a*b
# def subtract(a,b):
#     return a-b
# def divide(a,b):
#     # Handles diviosn by zero
#     if b == 0:
#         return "Error: Division by zero is not allowed"
#     return a/b

# def ask_user():

#     ''' In Python, a variable created inside a function, 
#     like a and b in ask_user(), is called a local variable. 
#     This means that a and b exist only within the 
#     ask_user() function.'''
   
    # a = float(input("Enter first number "))
    # b = float(input("Enter second nuber "))
    # operator =input("Choose operation (+,-,*,/)")
    # if operator == '+':
    #     result = add(a, b)
    # elif operator == '-':
    #     result = subtract(a, b)
    # elif operator == '*':
    #     result = product(a, b)
    # elif operator == '/':
    #     result = divide(a, b)
    # else:
    #     # If the operator is not valid, set an error message
    #     result = "Error: Invalid operator."

    #     # Step 3: Display the result
    # print("Result:", result)

# ask_user()  
# """ask_user() defines a and b inside itself, 
#  it knows what a and b are and doesn't need 
#  them as parameters from outside the function."""

# numbers = [1,2,3,4,5,6,7,8,9,10]
# for i in numbers: # for loop to iterate through list
#     if i%2 == 0: # to check if number is even
#         print(f"{i} is even")
#     else:
#         print(f"{i} is odd")

     
# def separate_even_odd(numbers):
#     even_numbers = []
#     odd_numbers = []
#     for number in numbers:
#         if number%2 == 0:
#             even_numbers.append(number)
#         else:
#             odd_numbers.append(number)

#     return even_numbers, odd_numbers
        
# numbers = [1,2,3,4,5,6,7,8,9,10]
# evens ,odds = separate_even_odd(numbers)
# print("even numbers:", evens)
# print("odds numbers:", odds)


# def separate_odd_even(numbers):
#     even_numbers = []
#     odd_numbers = []
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             odd_numbers.append(number)
#     return even_numbers, odd_numbers


# numbers = [1,2,3,4,5,6,7,8,9,10]
# evens, odds = separate_odd_even(numbers)
# print("even numbers:", evens)
# print("odds numbers:", odds)

# first_half_of_odd_numbers = odds[:len(odds)//2]
# first_half_of_even_numbers = evens[0:len(evens)//2]

# print(first_half_of_even_numbers)

# def add(a,b):
#     return a+b
# def product(a,b):
#     return a*b
# def ask_user():
#     a= float(input("Enter first numbe "))
#     b= float(input("Enter second number "))
#     operator = input("Enter operator: (+,-,*,/)")
#     if operator == "+":
#         result = add(a,b)
#     elif operator == "*":
#         result = product(a,b)
#     else:
#         result = "Error: Invalid operator"
#     print("Result:",result

# ask_user()

# def separate_even_odd(numbers): # separate_even_odd is a function which will take numbers as input
#     even_numbers = []  # empty list that will be filled later by classified numbers
#     odd_numbers = []
#     for number in numbers: # number is loop variable to iterate through the list numbers one by one
#         if number % 2 == 0:
#             even_numbers.append(number) # while iteration when even number is found it will be appended to respective list
#         else:
#             odd_numbers.append(number)
#     return even_numbers, odd_numbers
# numbers = [1,2,4,6,7,865,476,35,678,454,878,3,6,9,8,7,6,5,4,64,68,66.7,77.34,45.45,3,6.8,8.8]
# # print(separate_even_odd(numbers)) # this will print list in tupple form
# evens, odds = separate_even_odd(numbers) # unpacking to print separate list
# print("even numbers:", evens)
# print("odd numbers:", odds)

#  HARD CODE

# def separate_even_odd(): #without parameters
#     even_numbers = []
#     odd_numbers = []
#     for number in range(1,56): #hard coding meaning it has fixed range(no parameters needed)
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             odd_numbers.append(number)
#     return even_numbers, odd_numbers

# evens, odds = separate_even_odd()
# print("Evens numbers:", evens)
# print("odd numbers:", odds)

#SOFT CODE
# def separate_even_odd(custom_range): # soft code or parameterization
#     even_numbers = []
#     odd_numbers = []
#     for number in custom_range:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             odd_numbers.append(number)
#     return even_numbers, odd_numbers

# evens, odds = separate_even_odd(range(1,101))
# print(evens)
# print(odds)





# def add(a,b):
#     return a+b
# def product(a,b):
#     return(a*b)
# def subtract(a,b):
#     return a-b
# def divide(a,b):
#     if b == 0:
#         return("Invalid value, cant divide by zero")
#     else:
#         return a/b
# def ask_user():
    
#     a = float(input("Enter first number: ")) # This "a" is specific to the ask_user() function and does not directly interact with the "a" in the arithmetic functions.
#     b = float(input("Enter second number: "))
#     operator = input("Enter the operator (+, *, /, -): ")
#     if operator == "+":
#         result = add(a,b) # a and b are positional argumets
#     elif operator == "*":
#         result = product (a,b)
#     elif operator == "-":
#         result = subtract (a,b)
#     elif operator == "/":
#         result = divide (a,b)
#     else:
#         result = "Invalid operator"

#     print(f"The result of {a} {operator} {b} is: {result}")

# ask_user()
 
# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def product(a,b):
#     return(a*b)
# def divide(a,b):
#     if b == 0:
#         return "ERROR: Division by zero is not allowed" 
#     else:
#         return a/b
# def square(a):
#     return a**2
    
# def ask_user():
#     a = float(input("Enter first number: "))
#     operator = input("Enter operator (+, -, * , /, **)")
     
#     if operator in ["+", "-", "*", "/"]: # this condition is to escape the unnecessary  prompt for b 
#         b = float(input("Enter second number: "))

    
#         if operator == "+":
#             result = add(a,b) #result will hold the value of funtion add()
#         if operator == "-":
#             result = subtract(a,b)
#         if operator == "*":
#             result = product(a,b)
#         if operator == "/":
#             result = divide(a,b)
#         print(f"The result of {a} {operator} {b} is: {result}")
#     elif operator == "**":
#         result = square(a)
#         print(f"The result of {a} squared is: {result}")
#     else:
#         print("ERROR: Invalid operator")
        

# ask_user()

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def product(a,b):
    return(a*b)
def divide(a,b):
    if b == 0:
        return "ERROR: Division by zero is not allowed" 
    else:
        return a/b
def square(a):
    return a**2
    
def ask_user():
    a = float(input("Enter first number"))
    operator = input("Enter operator (+,-,/,*,**)")
    
    if operator in ["+", "-", "*", "/",]:
        b = float(input("Enter second number"))

        if operator == "+":
            result = add(a,b) #result will hold the value of funtion add()
        if operator == "-":
            result = subtract(a,b)
        if operator == "*":
            result = product(a,b)
        if operator == "/":
            result = divide(a,b)
        
        print(f"The result of {a} {operator} {b} is: {result}")

    elif operator == "**":
        print("")



    
















    







