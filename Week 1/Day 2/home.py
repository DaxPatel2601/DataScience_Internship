import random
import string

# user can sign in with new email and password , user can log in with email and also user can change password to

def main():
    email, password = signin_main()
    login_main(email, password)
    password = password_change(password)
    print(f"\nYor email is [{email}] and password id [{password}]\n")

def signin_main():
    print("\n[sign-in process is start] \n")
    sign_in = False
    email = str(input("Enter Your Email here:"))
    password = str(input("Enter Your Password here:"))
    otp = generate_otp()
    user_otp = str(input("varify your email though OTP:"))
    signin(email, password, user_otp, otp)
    return email,password

def login_main(email,password):
    print("[login process is start]\n")
    user_entered_email = input("Enter your email : ")
    user_entered_password = input("Enter Your Password:")
    log_in = False
    login(user_entered_email, user_entered_password,email,password)

def password_change(password):
    print("\n[Change password process is start]\n")
    # program for changing password
    new_password = ""

    entered_old_password = str(input("Enter Your Old Password:"))
    if entered_old_password != password:
        print("Enter password is wrong!!")
    else:
        new_password = str(input("Enter yor new password:"))
        if new_password == password:
            print("Entered new password is same as old password , please change your password")

        reenter_new_password = str(input("ReEnter Your New Password:"))
        if reenter_new_password == new_password:
            print("{New Password is ready to use.....}")
            return new_password

        elif reenter_new_password != new_password:
            print("ReEnter Password is Different from New Password")

def generate_otp():
    characters = string.digits
    otp = ''.join(random.choice(characters) for i in range(4))
    print("OTP is :",otp)
    return otp

def signin(email,password,user_otp,otp):

   if user_otp==otp:
       print("{You have successfully sign in}\n")
       sign_in=True
   else:
       print("OTP can not be match , please try again")
       sign_in=False

def login(user_entered_email,user_entered_password,email,password):
    if user_entered_email== "" and user_entered_password!= "":
        print("Email can not be blank")
        log_in = False
    elif user_entered_email != "" and user_entered_password == "":
        print("Password can not be blank")
        log_in = False
    elif user_entered_email == "" and user_entered_password == "":
        print("email and password can not be blank")
        log_in = False
    else:
        if user_entered_email == email and user_entered_password == password:
            print("{You have Successfully login}")
            log_in = True
        else:
            if user_entered_email != email and user_entered_password != password:
                print("Invalid email and Password")
                log_in = False
            elif user_entered_email != email:
                print("Enter Valid Email")
                log_in = False
            elif user_entered_password != password:
                print("Enter Valid Password")
                log_in = False

main()




