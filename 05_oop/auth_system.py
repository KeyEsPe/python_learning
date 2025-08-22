class User: 
    
    def __init__(self, login, password):
        self.login = login 
        self.password = password

class AuthSystem:

    def __init__(self):
        self.users = {}      # We use dictionary to store users and their passwords. 

    def register_user(self, username, password):
        if username in self.users:    # Check if the user is already registerd
            print("Username already exists!")
            return False     # Using return T/F we return the information for the program if the operation was or was not sucessfull. 
        new_user = User(username, password)    # Create variable new user which is an instance of the User class. 
        self.users[username] = new_user   # And we add to our dictionary WHOLE OBJECT new_user which contain username and password. 
        print(f"User {username} registered successfully!")
        return True
    
    def login(self, username, password):
        if username in self.users:     # We check if username is in our dictionary. 
            user_object = self.users[username]   # We create new variable to store whole object username from our dictionary of users. 
            if user_object.password == password:  # There is only need to check the password, because username matches, since we used it to fetch data. 
                print("You logged in successfully.")
                return True
            else:
                print("Invalid login or password")
                return False
        else:
            print("Invalid login or password")
            return False
        
    def list_users(self):
        return self.users.keys()   # This method is used to print out all our users since usernames are keys in the dictionary. 
                

auth_system = AuthSystem()

auth_system.register_user("Katarzyn", "Password123")
auth_system.register_user("Friso", "Mistery123")
auth_system.register_user("Linux", "Unknown123")
auth_system.register_user("Katarzyn", "Password123")

auth_system.login("Katarzyn", "Password123")
auth_system.login("Friso", "Password123")

print("Registered users: \n" , auth_system.list_users())
