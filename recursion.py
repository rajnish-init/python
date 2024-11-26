#recursive function
# def show (n):
#     if n == 0:
#         return
#     print(n)
#     show(n-1)


# show(5)

# def show (n):
#     if n == 0:
#      return
#     print(n)
#     show(n-1)
#     print("END")

# show(3) 

#factorial
# def fact(n):
#    if (n == 0 or n == 1):
#       return 1
#    return fact(n-1)*n

# print(fact(6))

# def cal_sum(n):
#     if n == 0:
#         return 0
#     return cal_sum(n-1)+n
    

# sum = cal_sum(5) 
# print(sum)


# def calc_sum(n):
#     if n ==0:
#         return
#     print(n)
#     calc_sum(n-1)

# calc_sum(5)

# def calc_sum(n):
#     if n == 0:
#         return 1
#     else:
#         print(n)
#         calc_sum(n-1)

# calc_sum(5)

    
def calc_sum(n):
    if n == 0:
        return 
    else:
        return calc_sum(n-1)+n

sum = calc_sum(5)
print(sum)

