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

def separate_even_odd(numbers): # separate_even_odd is a function which will take numbers as input
    even_numbers = []  # empty list that will be filled later by classified numbers
    odd_numbers = []
    for number in numbers: # number is loop variable to iterate through the list numbers one by one
        if number % 2 == 0:
            even_numbers.append(number) # while iteration when even number is found it will be appended to respective list
        else:
            odd_numbers.append(number)
    return even_numbers, odd_numbers
numbers = [1,2,4,6,7,865,476,35,678,454,878,3,6,9,8,7,6,5,4,64,68,66.7,77.34,45.45,3,6.8,8.8]
# print(separate_even_odd(numbers)) # this will print list in tupple form
evens, odds = separate_even_odd(numbers) # unpacking to print separate list
print("even numbers:", evens)
print("odd numbers:", odds)





    







