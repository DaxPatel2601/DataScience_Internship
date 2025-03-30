# logic for login page


def login(email,password):
    if email == "" and password != "":
        print("Email can not be blank")
        log_in = False
    elif email != "" and password == "":
        print("Password can not be blank")
        log_in = False
    elif email == "" and password == "":
        print("email and password can not be blank")
        log_in = False
    else:
        if email == "a@b.com" and password == "abc123":
            print("Login Successful")
            log_in = True
        else:
            if email != "a@b.com" and password != "abc123":
                print("Invalid email and Password")
                log_in = False
            elif email != "a@b.com":
                print("Enter Valid Email")
                log_in = False
            elif password != "abc123":
                print("Enter Valid Password")
                log_in = False


email=input("Enter your email : ")
password=input("Enter Your Password:")
log_in=False
login(email,password)

