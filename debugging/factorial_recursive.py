#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the number from command-line arguments
if len(sys.argv) != 2:
    print("Usage: ./factorial_recursive.py <non-negative integer>")
    sys.exit(1)

number = int(sys.argv[1])
if number < 0:
    print("Error: Please provide a non-negative integer.")
    sys.exit(1)

# Compute factorial and print the result
f = factorial(number)
print(f)