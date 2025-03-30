ac=["ON","OFF"]

is_ac_on="off"

while True:
    user_input = input("ON|OFF : ").upper()
    if user_input!="STOP":
        if user_input==ac[0] and is_ac_on=="on":
            print("AC is already on!!")

        elif user_input==ac[1] and is_ac_on=="off":
            print("AC is already off!!")

        elif user_input==ac[0] and is_ac_on=="off":
            print("AC is Now On")
            is_ac_on="on"

        elif user_input==ac[1] and is_ac_on=="on":
            print("Ac is now OFF")
            is_ac_on="off"

    else:
        break

