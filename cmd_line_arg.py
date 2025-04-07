import sys
import os

print('argument list', sys.argv)

name = sys.argv[1]

def greet(name):
    return f"hello, {name}"

print(greet(name))

first = int(sys.argv[2])
second = int(sys.argv[3])

#print("sum is: {}".format(first+second))
print(f"sum is: {first + second}")