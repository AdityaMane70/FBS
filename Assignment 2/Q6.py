# 6. WAP to calculate total salary of employee based on basic, da=10% of basic, 
# ta=12% of basic, hra=15% of basic.
basic=int(input("Enter basic salary:"))

ba=basic*(10/100)
ta=basic*(12/100)
hra=basic*(15/100)
total_salary=basic+ba+ta+hra

print(f"total salary after ba,ta and hra is {total_salary}")
