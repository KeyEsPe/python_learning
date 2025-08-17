class BankAccount:     # We create a new class
    def __init__(self, owner, balance):     # Any object in our new class will have two attributes: owner and balance. 
        self.owner = owner
        self.balance = balance 

    def deposit(self, amount):     # We create a method which will have one parameter - amount. It's without "self" because this is the parameter we pass to the method, not the object attribute.  
        self.balance = self.balance + amount    # We using "Self" for balance, becuase we want that the main attribute will be permanently updated. 
        print(f"\nThank you {self.owner} for your {amount} deposit. Your current saldo is {self.balance}")
    
    def withdraw(self, amount):    # We create a new method and we can use the same names of variables in different methods. 
            if amount > self.balance:
                print("Not enough money. Please try again")
            else:
                self.balance = self.balance - amount
                print(f"Withdrawal was successful. Your current saldo is {self.balance}")
    
    def get_balance(self):     # Method get_balance has only standard parameter, which refers to object instance, in this case balance. 
        print(f"Your current balance is {self.balance}")    
                
                

owner1 = BankAccount("Katarzyn", 100)    # Creation of new object, owner name and her balance. 
owner1.deposit(200)    # We use our deposit method and pass 200 as amount. 
owner1.withdraw(50)  # Here we use our withdraw method and pass 50 as an argument. 
owner1.get_balance()  
