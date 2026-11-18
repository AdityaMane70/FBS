# 7. Program to Find the Roots of a Quadratic Equation
# equation x*2+2x=5
a=int(input("enter a:"))
b=int(input("enter b:"))
c=int(input("enter c:"))

r1= (-b+((b**2)-(4*a*c))**0.5)/(2*a)
r2= (-b-((b**2)-(4*a*c))**0.5)/(2*a)
print(f"root of quadtratic equation are {r1} and {r2}")
