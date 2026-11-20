# 7. Write a program to prompt user to enter userid and password. After verifying 
# userid and password display a 4 digit random number and ask user to enter the 
# same. If user enters the same number then show him success message otherwise 
# failed. (Something like captcha)
user_name=input("Enter your name:")
passward=input("Enter passward:")
if user_name=="aditya" and passward=="12":
    num=4567
    print("your captcha is:",num)
    captcha=int(input("enter captcha:"))

    if captcha==num:
        print("Login successfull")
    else:
        print("Login Failed")
else:
    print("enter vavlid input")