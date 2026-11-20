# 11. Write a program to check if given 3 digit number is a palindrome or not.
number=int(input("enter any three digit number:"))
last_digit=number%10 # give last digit
digit1=number//10    # give first two digits

second_digit=digit1%10 # give second digit
first_digit=digit1//10 # give first digit

palin=(last_digit*100)+(second_digit*10)+(first_digit)
if number==palin:
    print(f"{number} is an palindrome number")
else:
    print(f"{number} is not an palindrome")