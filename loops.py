# while True:
#     print("hello")
    
# count = 1
# while count <= 100 :
#     print("hello",count)
#     count += 1   #count = count +1

# print numbers from1 to 5
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

# print("Loop ended.")

#practice questions
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

# i = 100
# while i >= 1: # stopping condition
#     print(i)
#     i -= 1
  
# i = 9
# while i <= 90:
#     print(i)
#     i += 9

# i = 1
# n =int(input("enter number : "))
# while i <=10:
#     print(n*i)
#     i += 1

# i = 1
# while i <= 10:
#     print(16*i)
#     i += 1

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

 
# idx = 0
# while idx < len(nums):
#     print(idx )
#     idx += 1

#while loop
# nums = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i< len(nums):
#     print(nums[i])
#     i += 1

#for loop
# nums = [1,4,9,16,25,36,49,64,81,100]

# for el in nums:
#     print(el)

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 81

# i = 0
# for el in nums:
#     if el == x:
#         print("number found at index: ", i)
#     i += 1

# for i in range(100,0,-1):
#     print(i)

# nums = [1,2,3,4,5,6,7,8,9]
# for el in nums:
#     print(el)

# for i in range(5):
#     print("hello")

# i = 100 
# while i >= 1:
#     print(i)
#     i -= 1

# n = int(input("enter number."))
# i = 1
# while i<=10:
#     print(n*i)
#     i+=1

# nums = [1,4,9,16,25,36,49,64,81,100]
# i = 0        # using i as an index to access each element from 0 to the last index in the list.
# while i < len(nums):
#     print(nums[i])     #print nums at ith index; nums[0],nums[1]...
#     i += 1

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 64
# i = 0
# while i < len(nums):
#     if nums[i] == x: 
#         print("found at index :", i)
#     else:
#         print("finding...")

#         # break # Stop the loop once we find the value
#     i += 1

# nums = (1,4,9,16,25,36,49,64,81,100)
# target = 64
# for num in nums:
#     if num == target:
#         print("found target:", 64)
#         break    # Exits the loop as soon as target is found
#     print("checking number:",num)

# nums = (1,4,9,16,25,36,49,64,81,100)
# for num in nums:
#     if num%2 == 0: #even numbers
#         continue   # Skips this iteration if num is even
#     print("odd number:", num)

# nums = (1,4,9,16,25,36,49,64,81,100)
# for num in nums:
#     if num%2 != 0: #odd numbers
#         continue   # Skips this iteration if num is odd
#     print("even number:", num)


# # sum of n numbers 
# n = 7     # 1+2+3+4+5+6+7
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print("total sum is :", sum)


# n = 7     
# sum = 0
# for i in range(1, n + 1):
#     sum += i  # Adds each number to sum

# # This print statement is now outside the loop to print the final sum
# print("total sum is :", sum)


# nums = [1,4,9,16,25,36,49,64,81,100]
# for el in nums:
#     print(el)

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 81
# for i in nums:
#     if i == 81:
#      print("found at index:", i)



# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 64
# i = 0
# while i < len(nums):
#     if nums[i] == x: 
#         print("found at index :", i)
#     else:
#         print("finding...")

#         # break # Stop the loop once we find the value
#     i += 1

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 81
# i = 0
# while i < len(nums):
#     if nums[i] == x:
#      print("found at index:", i)
#     i += 1

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 9
# i = 0
# while i < len(nums):
#     if nums[i] == x:
#      print("found at index:", i)
#      break
#     else:
#      print("finding...")
#     i+=1

nums = (1,4,9,16,25,36,49,64,81,100)
x=81


# for i in range(len(nums)):
#     if nums[i] == x:
#         print("found at index:", i)
#         break
#     else:
#         print("finding....")


# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 4
# for i in range(len(nums)):         #iterates through each index of nums.
#     if nums[i] == x:               #checks if the current element is equal to x.
#         print("found at index:",i)
#         break                      #break stops the loop once the match is found.
#     else:
#         print("finding....")       #The else statement prints "finding..." until it finds the match.

# n = 4
# for i in range(1,n+1):
#     print()
            


# n = 5
# sum = 0
# for i in range(1,n+1):
#     sum +=i
# print("sum is:",sum) 

# n = 4 
# sum = 0
# i = 1
# while i <=n:
#     sum+= i
#     i+=1
# print("fact is =",sum)

# n = 5
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print("factorial is =", fact)

# n = 9 
# fact  = 1
# i = 1
# while i <=n:
#     fact*=i
#     i+= 1
# print("factorial is =", fact)


# n = 20
# for i in range(1,n+1):
#     if i%2 == 0:
     
#      print(i)



# n = 10
# sum = 0
# for i in range(1,n+1):
#    sum+=i
   
# print("the sum is:", sum)



# n = 10 
# while n>=1:
#    print(n)
#    n -= 1
#    if n ==0:
#     print("Liftoff!")




n =int(input("enter number "))
for i in range(1,11):
        print(n*i)



# n = 50
# sum = 0
# for i in range(1,n+1):
#         if i%2 != 0:
#                 sum+=i
# print("the sum of odd numbers from 1 to 50 is:",sum)


# n = 1
# sum = 0
# while n<=4:
#     sum+=n
#     n+=1                  

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
        p