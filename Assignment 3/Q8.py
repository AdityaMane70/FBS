# 8. Input 5 subject marks from user and display grade(eg.First class,Second class ..)
subj1=int(input("enter marks of subject 1:"))
subj2=int(input("enter marks of subject 2:"))
subj3=int(input("enter marks of subject 3:"))
subj4=int(input("enter marks of subject 4:"))
subj5=int(input("enter marks of subject 5:"))
percentage=((subj1+subj2+subj3+subj4+subj5)/500)*100
if (percentage>85):
    print("you have got first class marks")
elif (percentage>70 and percentage<85):
    print("you have got second class marks")
elif (percentage>55 and percentage<70):
    print("you have got third class marks")
elif (percentage>35 and percentage<55):
    print("you have got fourth class")
else:
    print("you are failed")