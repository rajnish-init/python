# a = int(input("enter 1st number "))
# b = int(input("enter 2nd number "))
# c = int(input("enter 3rd number "))
# if a == b == c:
#     print("all three numbers are equal")
# elif a >= b and a >= c:  # here both condition need to be true to print the result because of AND operator
#     print("a is the greatest")
# elif b >= a and b >= c:
#     print("b is the greatest")
# else:
#     print("c is the greatest")

#Q2
# a = int(input("Enter a number: "))
# if a % 7 == 0:
#     print(f"{a} is a multiple of 7.")
# else:
#     print(f"{a} is not a multiple of 7")

# def ask_user():
#     my_movies_list = []
#     first =input("enter your first favourite movie: ")
#     second =input("enter your second favourite movie: ")
#     third =input("enter your third favourite movie: ")
#     my_movies_list.append(first)
#     my_movies_list.append(second)
#     my_movies_list.append(third)
#     return my_movies_list  #  when you call the function ask_user, it will return My_movies_list containing the movies list
# # movies = ask_user()
# # print(", ".join(movies))          # to print simply wothout any brackets
# # print(movies)

# print(ask_user())

#FizzBuzz
#

# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%5 == 0:
#         print("Buzz")
#     elif i%3 == 0:
#         print("Fizz")
#     else:
#         print(i)

#Using While loop

# i = 1  
# while i <= 50:

#     if i%3 == 0 and i%5 == 0:
#         print("FizzBuzz")
#     elif i%3 ==0:
#         print("Fizz")
#     elif i%5 ==0:
#         print("Buzz")
#     else:
#         print(i)
#     i += 1


    
#Temperature conversion

# def kelvin_to_celsuis(kelvin):
#     celsius = kelvin - 273.15
#     return celsius  # #Once the value is returned, Python cleans up the function’s workspace (local variables are destroyed).

# kelvin_value = float(input("Enter temperature in kelvin: ")) #This line is not part of the function because the function block was already closed (the indentation level decreased after return celsius)

# celsius_value = kelvin_to_celsuis(kelvin_value)

# print(f"The temperature in celsius is: {celsius_value} degree celsius")

# def kelvin_to_celsius(kelvin):
#     celsius = kelvin - 273.15
#     return celsius # used return the value upon function call.
# kelvin_value = float(input("Enter temperature in kelvin: ")) 
# celsius_value = kelvin_to_celsius(kelvin_value) #putting kelvin_value as an argument to function and storing that value in the celsius_value.
# print(f"The temperature in kelvin is: {celsius_value}")


# numbers = []
# numbers.append(int(input("Enter first number: ")))
# numbers.append(int(input("Enter second number: ")))
# numbers.append(int(input("Enter third number: ")))
# numbers.append(int(input("Enter fourth number: ")))
# numbers.append(int(input("Enter fifth number: ")))
# print(numbers)


# numbers = []
# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# print("The numbers you entered are:", numbers)


# def kelvin_to_celsius(kelvin): # define a function which will take kelvin value as input
#     celsius = kelvin - 273.15  #here calculation happens and calculated value will be stored in celsius variable that is local variable
#     return celsius # clacutated value will be returned upon function call
# kelvin_value = float(input("Enter temperature value in kelvin: ")) # asking user to kevin input
# celsius_value = kelvin_to_celsius(kelvin_value) #creating this variable to store the value of function call
# print(f"the celsius vlaue of {kelvin_value} kelvin  is: {celsius_value}") # printing using formatting string

# n = 10
# while n >= 1 :
#     print(n)
#     n -= 1

for i in range(20,0,-1):
    """20: The starting number of the loop.
0: The stopping condition (not inclusive, so it stops at 1).
-1: The step size, which determines the decrement in each iteration."""
    print(i)

