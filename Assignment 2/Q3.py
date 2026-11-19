# 3. Convert distant given in feet and inches into meter and centimeter.
feet=int(input("enter the distance in feet:"))
inches=int(input("enter the distance in inches:"))

total_inches=(feet*12)+inches

centimeter=total_inches*2.54
meter=centimeter/100

print("distance in meter:",meter)
print("distance in centimeter:",centimeter)