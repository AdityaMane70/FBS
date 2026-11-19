# 1. Convert the time entered in hh,min and sec into seconds.
hours=int(input("enter hours:"))
min=int(input("enter minutes:"))
seconds=int(input("enter seconds:"))
total_seconds=hours*3600+min*60+seconds
print(f"total seconds in {hours} hours ,{min} minutes and {seconds} seconds is {total_seconds}")