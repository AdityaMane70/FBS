# 7. Find the sum of three-digit number.
number=int(input("enter an three digit numbr:"))
a=number%10
num=number//10

b=num%10
num=num//10

c=num%10
num=num//10

sum=a+b+c
print(f"sum of {number} three digits is {sum}")