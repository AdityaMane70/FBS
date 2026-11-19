# 9. Write a program to swap two numbers without using third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"bafore swapping a is {a} and b is {b}")

a,b=b,a

print(f"after swapping a is {a} and b is{b}")