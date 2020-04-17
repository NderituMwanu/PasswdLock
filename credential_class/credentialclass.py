class Credentials:
    """
    This class generates new instances of contacts
    """

    credentials_list = []  #empty list of stored credentials.
    def __init__(self,username,password):
        
        self.username = username
        self.password = password

    complete = False
    print("Enter your username")
    username = input()

    print("Enter your password")
    password = input()  
    
    print(username)
    print(password)



    
