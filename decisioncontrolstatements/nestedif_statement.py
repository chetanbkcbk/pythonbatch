age=int(input("enter the age"))
is_citizen=eval(input("is person a citizen?True/False"))
if age>18:
    if is_citizen:
        print("Eligible to Vote")
    else:
        print("Not Eligible to Vote")

else:
    print("UnderAge ,Not eligible to Vote ")