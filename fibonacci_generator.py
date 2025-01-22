# Python Script: Fibonacci Generator

def generate_fibonacci(n):
    """Generate a Fibonacci sequence up to n terms."""
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

# User input
try:
    terms = int(input("Enter the number: "))
    print("Fibonacci Sequence:", generate_fibonacci(terms))
except ValueError:
    print("Invalid input! Please enter a positive integer.")
