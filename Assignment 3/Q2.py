# 2. Write a program to input any alphabet and check whether it is vowel or consonant.
alpha=input("Enter alphabate:")
if (alpha in 'AEIOU'):
    print(f"{alpha} is an vowel")
else:
    print(f"{alpha} is an constant")