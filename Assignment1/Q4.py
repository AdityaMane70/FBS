# 4. Write a program to enter P, T, R and calculate simple Interest.
print("Example no 4")
p=int(input("enter principle value :"))
t=int(input("enter time value :"))
r=int(input("enter rate of interest :"))
SI=(p*r*t)/100
print(f"Simple interest on given {p} amount ,time {t} years and rate of interest {r}% is :{SI} \n ")