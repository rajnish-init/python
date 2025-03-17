def calc_sum(a,b):
    sum=a+b
    return sum
print(calc_sum(1,2))

def avg_3(a,b,c):
    avg=(a+b+c)/3
    return(avg)
avg_3(1,2,3)
print(avg_3(1,2,3))


# def avg(a,b): #function definition
#     avg=(a+b)/2 #function logic
#     print(avg) #function call

# avg(1,2) #function call


# def avg_3(a,b,c):
#     avg = (a+b+c)/3
#     user_input = int(input("Enter three numbers each separated by a comma: "))
#     return avg



# user_input = input("Enter Your Name: ")
# print(type(user_input))
# print(len(user_input))
# print(f"WELCOME TO LINUX Mr.",user_input.title())
# print(str(user_input[0:3]))
# num = int(input("Enter a number: "))
# if num%2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is odd")

num = [1,2,3,4,5,6,7,8,9,10]
print(num[1:10:2])


text = "python"
print(text[2:6])

alpha = "abcdefghijklmnopqrstuvwxyz"
print(alpha[1:27:2])
print(alpha[::-1])

lst = [1,2,3,4,5,6,7,8,9,10]
print(lst[::-1])

def cal_sum(a,b):
    sum = a+b
    print(sum)
    return sum
    
cal_sum(4,5)
result = cal_sum(4,5)
total = result + 10
print(total)

def find_max(*args):
    if args: # check if there are any arguments
        return max(args)
    return None
max_value = find_max(4,5,7,23,8,87,22,1,101) #example call
print(max_value)

# import os
# os.rename("temp.py","mixed-practice.py")

#loops

count = 1 #initialization
while count <= 5: #stop condition
    print(count)
    count += 1 #increment
print("done")

i = 1 #initialization
while i<= 10: #stop condition
    print(i*9) 
    i += 1 #increment


for i in range(2,50,2): #range(start,stop,step)
    print(i)

#sum of n numbers
n = 9 #stop condition
sum = 0 #initialization
for i in range(1,n+1): #range(start,stop)
    sum += i #increment (sum = sum + i)
print(f"The sum of Number is: ", sum)



#recursive function

def show(n):
    if n == 0: #base case
        return
    print(n)
    show(n-1) #recursive case
print("done")
show(5) #function call


god = ["shiva","vishnu","brahma","durga"]
def print_list(list):
    for item in list: # item is a loop variable, it takes the value of each element in the list
        print(item, end=" ")
print_list(god)
print()


def converter(usd_val):
    inr_val = usd_val * 83
    print(f"USD {usd_val} is equal to INR {inr_val}")

converter(100)

nums = (1,4,9,16,25,36,49,64,81,100)
target = 64
for num in nums:
    if num == target:
        print("found target at:", 64,"at index:",nums.index(64))
        break    # Exits the loop as soon as target is found
    print("checking number:",num)

def show (n): # function definition
    if n == 0: # base case
        return 
    print(n)
    show(n-1) # recursive case 
show(5) # function call

def reverse_list(lst):
    if lst == 5:
        return
    print(lst)
    reverse_list(lst-1)

reverse_list(10)

data = [1,2,3,4,5,6,7,8,9,10]
for i in data:
    if i == 5:
        print(f"found {i} at index: ", data.index(i))

