class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.logegin = False
        self.menu()
        
        
    def menu(self):
        user_input = input("""Welcome to the chatbook! How would you like to proceed?
                           1. Press 1 to Signup..
                           2. Press 2 to Signin..
                           3. Press 3 to write a post..
                           4. Press 4 to message a friend.. 
                           5. Press any other key to exit..
                           
                           Enter Input : """)
        if user_input == "1":
            self.signup()
        
        elif user_input == "2":
            self.signin()
        
        elif user_input == "3":
            self.mypost()
        
        elif user_input == "4":
            self.sendmsg()
        
        else:
            exit()
            
    def signup(self):
        email = input("Write your email here : ")
        pwd = input("Enter your password here : ")
        self.username = email
        self.password = pwd     
        print("You Have signedup sucessfully!")
        print("\n")
        self.menu()        
        
        
    def signin(self):
        if self.username=="" and self.password=="":
            print("Please signup first by pressing 1 in the main menu..")
            
        else:
            uname = input("Enter the email/username here : ")
            pwd = input("Enter the password : ")
            if self.username == uname and self.password==pwd:
                print("You have signedin sucessfully..")
                self.logegin = True
                
            else:
                print("Please input correct credentials..")
        print("\n")
        self.menu()
        
        
    def mypost(self):
        if self.logegin==True:
            txt=input("Enter the content to post : ")
            print(f"Following content has been posted {txt}..") 
            
        else:
            print("You need to signed in to post something..")  
    
    
    def sendmsg(self):
        if self.logegin==True:
            txt=input("Enter your msg here : ")
            frnd = input("Whom to send this msg? ")
            print(f"Your Message has been sent to {frnd} ")
            
        else:
            print("You need to signedin First to post something")
        print("\n")
        self.menu()
        
                    
obj = chatbook()