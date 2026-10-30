# 8. Write a program to convert days into years, weeks and days.
print("Example no 8")
Days=int(input("enter the number of days to be converted into years,weeks and days :"))
years=Days//365
print(f"years in {Days} days are {years}years")
days=Days%365
weeks=days//7
print(f"Number of weeks after calculating {years}years are {weeks}weeks")
daays=days%7
print(f"Remaining days after calculating {years}years ,{weeks}weeks are {daays}")
print(f"Years,weeks and days in {Days}days are {years}years,{weeks}weeks,{daays}days\n")