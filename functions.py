def calc_sum(a,b):
    sum = a+b
    print(sum)
    return sum

def avg_3(a,b,c):
    avg = (a+b+c)/3
    print(avg)
    

avg_3(82,88,91,)

def avg_3(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)

cities = ["delhi", "patna", "noida", "mumbai", "chennai"]
god = ["shiva", "krishna", "hanuman", "bramha"]

def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end="   ")


print_list(cities)

def cal_fact(n): 
    fact = 1
    for i in range(1, n+1):
        fact*=i
    print(fact)

cal_fact(6)


#return and without return
def cal_sum(a,b):
    sum = a+b
    print(sum)
    return sum
    
cal_sum(4,5)
result = cal_sum(4,5)
total = result + 10
print(total)


def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val, "USD=", inr_val, "INR")

converter(83)

god = ["shiva", "kaali", "krishna", "hanuman", "bramha",]
def print_el(list):
    for el in list:
        print(el,end=" ")

god.insert(1,"chandi")

print_el(god)

god = ["shiva", "kaali", "krishna", "hanuman", "bramha",]
def print_el(list):
    for el in list:
        print(el,end=" ")
god.insert(3,"chandi")
print_el(god)

god = ["shiva", "kaali", "krishna", "hanuman", "bramha",]
def print_len(list):
    god.append("vishnu")
    print(len(list))
    
    


god = ["shiva",3, "kaali", "krishna", "hanuman", "bramha",]
def print_len(el):
    el.append("vishnu")
    print(len(god))

print_len(god)


# n = int(input("enter a number "))
def identifier(n):
    if n%2 == 0:
        print(n, " is even")
    else:
        print(n, "is odd")
    
# identifier(n)

    
def is_even(n):
    if n%2 == 0:
        return True
    return False

print(is_even(89))


def fact(n):
    if n == 0:
        return 1
    print(n)
    return fact(n-1) *n
    
print("factorial is = ",fact(5))

def square(n):
    return n * n
result = square(55)
print("the square of 5 is:", result)

def greet_person(name,age):
    print(f"hello, {name} you are {age} years old")

greet_person("rajnish", 25)

def is_even(n):
    return n%2 == 0

print(is_even(4))

def find_max(*args):
    if args:# check if there are any arguments
        return max(args)
    return None
max_value = find_max(4,5,7,23,8,87,22,1) #example call
print(max_value)

def sum_range(a,b):
    if a > b:   # Step 1: Check if a is greater than b
        a,b = b,a   # Step 2: If yes, swap a and b
    return sum(range(a,b+1))    # Step 3: Sum the numbers from a to b (inclusive)
print(sum_range(1,5))

def power(base, exp):
    return base ** exp

print(power(2,2))


def is_Greater(a,b):
    if a>b:
        print("First is greater than the second: ")
    else:
        print("second is greater than or equal to First")
def is_Lower(c,d):
    if c<d:
        print("First is lower than second")
    else:
        print("second is lower than or equal to first")



is_Greater(5,7)
is_Lower(4,5)

# #defaul arguments
# def greet(name="Guest", age="old enough to be here."):
#     print(f"Hello, {name}! You are {age} .")

# greet() #uses default values
# greet("anand") # uses default age
# greet("raj", 21) #Overrides both defaults 

# keyword arguments
def greet(age=21, name="ved"):
    print(f"Hello, {name}! You are {age} years old.")

greet() #uses default values
greet(age=23, name="bruno") #uses keyword arguments

print("Apple", "Banana", "Cherry", sep=", ", end="!")
print()

print("Hello",end=" ")
print("World")
print()

for i in range(3):
    print(i, end="\n")

def add_numbers(*numbers):
    total = sum(numbers)
    print("sum is:", total)
add_numbers(1+2+3+4+5)
add_numbers(23+234+54+324)

