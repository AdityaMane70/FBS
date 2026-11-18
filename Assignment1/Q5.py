# 5. Write a program to enter P, T, R and calculate Compound Interest.
print("Example no 5")
p=int(input("enter principle value :"))
t=int(input("enter time value :"))
r=int(input("enter rate of interest :"))
CI=(p*(1+(r/100))**t)-p
print(f"compound interest on given {p} amount ,time {t} years and rate of interest {r}% is :{CI} \n ")