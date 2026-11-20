# 9. Write a program to check if person is eligible to marry or not (male age >=21 and 
# female age>=18)
gender=input("Enter your gender (M/F):")
if gender=='M':
    age=int(input("enter age:"))
    if age>=21:
        print("boy is eligible to marriage")
    else:
        print("boy is not eligible for marriage")
else:
    age=int(input("enter your age:"))
    if age>=18:
        print("girl is eligible for mirrage")
    else:
        print("girl is not eligible for mirrage")