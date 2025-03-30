# logic for change password


def password_change(password):
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
            print("New Password is ready to go")
            return new_password

        elif reenter_new_password != new_password:
            print("ReEnter Password is Different from New Password")




password="abc123"
password=password_change(password)
print(password)