# 11. Write a program to accept an integer amount from user and tell minimum 
# number of notes needed for representing that amount.
amount=int(input("enter the amount:"))
note500=amount//500
note=amount%500

note200=note//200
note2=note%200

note100=note2//100
note3=note2%100

note50=note3//50
note4=note3%50

note20=note4//20
note5=note4%20

note10=note5//10
note6=note5%10

note5=note6//5
note7=note6%5

note2=note7//2
note8=note7%2

note1=note8//1

print(f"minimum number of notes required for {amount} amount is {note500+note200+note100+note50+note20+note10+note5+note2+note1}")