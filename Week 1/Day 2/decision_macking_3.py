# logic for sign in

import random
import string

def generate_otp():
    characters = string.digits
    otp = ''.join(random.choice(characters) for i in range(4))
    print(otp)
    return otp


def signin(email,password,user_otp,otp):
   print(otp)
   if user_otp==otp:
       print("you have successfully sign in")
       sign_in=True
   else:
       print("OTP can not be match , please try again")
       sign_in=False

sign_in=False
email=str(input("Enter Your Email here:"))
password=str(input("Enter Your Password here:"))
otp = generate_otp()
user_otp=str(input("varify your email though OTP:"))
signin(email,password,user_otp,otp)

