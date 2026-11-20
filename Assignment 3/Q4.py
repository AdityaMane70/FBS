#4.Write a program to check whether the triangle is equilateral, isosceles or scalene 
# triangle.
a1=int(input("Enter first angle of triangle:"))
a2=int(input("Enter second angle triangle:"))
a3=int(input("Enter thirt angle of triangle:"))
if (a1+a2+a3==180):
    print("Triangle is valid triangle")
    if(a1==a2) or (a2==a3) or (a1==13):
        print("Triangle is Isoscale triangle")
    elif (a1!=a2!=a3):
        print("Triangle is scalene triangle")
    else:
        print("triangle is equilateral")
else:
    print("Triangle is invalid")