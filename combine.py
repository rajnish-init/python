import sys
import os

print('argument list', sys.argv)

name = os.environ.get("MY_NAME")
cred = os.environ.get("PASSWORD")
if name is None and len(sys.argv) > 1:
    name = sys.argv[1]
    
if name is None:
    name = "Guest"

# cred = sys.argv[1]

def greet(name,):
    return f"Hello, {name}"

print(greet(name))