# 10. Write a program to reverse three-digit number.
num=132

last=num%10
num=num//10

second=num%10
num=num//10

third=num%10
num=num//10

reversed_num=(last*100)+(second*10)+third
print("reversed number is:",reversed_num)