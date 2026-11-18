# 8. Write a program to convert days into years, weeks and days.
print("Example no 8")
Days=int(input("enter the number of days to be converted into years,weeks and days :"))
years=Days//365
days=Days%365
weeks=days//7
daays=days%7
print(f"Years,weeks and days in {Days}days are {years}years,{weeks}weeks,{daays}days\n")