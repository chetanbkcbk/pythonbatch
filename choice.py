from user import User
while True:
    print("-------\n Welcome to Dheecoding lab\n Enter 1 if u r new and wish to register \n Enter 2 if u already are student and want to login \n Enter 3 to exit\n -------")

    c=int(input("Enter the choice"))

    if c==1:
        un=input("Enter the username")
        p=input("Enter the password")
        fn=input("Enter the f_name")
        e=input("Enter the email")

        user1=User(un,p,fn,e)
        User.register_user(user1)

    elif c==2:
        un=input("Enter the username")
        p=input("Enter the password")
        for user in User.users:
            if un==user.username and p==user.password:
                print(f"Welcome {user.username} ") #if else will work if i have 1 user in list ,to check for all users ,i shud make use of for else loop
                break
        else:
                print("please enter correct credentials")
        
    elif c==3:
        print("you are exiting the application")
        break
    else:
        print("invalid choice")