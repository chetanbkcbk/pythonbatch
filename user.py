class User:
    users=[]

    def __init__(self,username,password,f_name,email):
        self.username=username
        self.password=password
        self.f_name=f_name
        self.email=email
        

    @staticmethod
    def check_password(password):
        return len(password)>=8 and password.isalnum()
    
    @classmethod
    def register_user(cls,user):
        if User.check_password(user.password):
            print("User registered Successfully")
            User.users.append(user)
        else:
            print("enter correct password format")


'''user1=User("cbk","chetanbk123","chetan byaladakere Krishnegowda","chetanbkcbk@gmail.com")

User.register_user(user1)
print(User.users[0].f_name)'''