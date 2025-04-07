import os 

name = os.environ["MY_NAME"] # fetch the environment variable 

def greet(name):
    return f"Hello, {name}"
    
print(greet(name))