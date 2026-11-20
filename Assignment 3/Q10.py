# 10. Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.
total=0
age1=int(input("enter your age:"))
age2=int(input("enter your age:"))
age3=int(input("enter your age:"))
age4=int(input("enter your age:"))
age5=int(input("enter your age:"))
amount=float(input("enter price per person:"))

if age1<12:
    total=total+amount*0.70
elif age1>59:
    total=total+amount*0.50
else:
    total=total+amount

if age2<12:
    total=total+amount*0.70
elif age2>59:
    total=total+amount*0.50
else:
    total=total+amount

if age3<12:
    total=total+amount*0.70
elif age3>59:
    total=total+amount*0.50
else:
    total=total+amount

if age4<12:
    total=total+amount*0.70
elif age4>59:
    total=total+amount*0.50
else:
    total=total+amount

if age5<12:
    total=total+amount*0.70
elif age5>59:
    total=total+amount*0.50
else:
    total=total+amount

print("total ticket price for all five member is:",total)