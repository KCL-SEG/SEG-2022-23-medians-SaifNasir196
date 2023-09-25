"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        
        numbers.sort()
        # print(numbers)
        print(numbers[len(numbers)//2])
        
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

