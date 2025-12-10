


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposite(self, amount):
        if amount < 0:
            print("Amount cannot be negative.")
        else:
            self.balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount < 0:
            print("Amount cannot be negative.")
            
        elif amount > self.balance:
            print("Insufficient Balance! Cannot withdrawn.")
            
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            
    def check_balance(self):
        print(f"Current Balance: {balance}")
            
name = input("Enter account holder's name: ")
balance = int(input("Enter your initial balance: "))   
    
account = BankAccount(name, balance)
 
        
while True:
    
    
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    choice = int(input("Enter a choice between(1-4): "))
    
    if choice == 1:
        amount = int(input("Enter the amount to deposite: "))
        account.deposite(amount)

    elif choice == 2:
        amount = int(input("Enter the amount to withdraw: "))
        account.withdraw(amount)
        
    elif choice == 3:
        account.check_balance()
    
    elif choice == 4:
        print("You exited the program.")
        break
    
    else:
        print("Invalid Operation!!")
        
