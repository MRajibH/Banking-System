'''
|BankManagement.py is a prototype banking system where user can create account, deposit and withdraw money, check balance and see their respective personal information.
|
| Project Name : Banking Mangement System
| Developed by : BroTecs Technologies Limited
| created      : May 06, 2021 
| updated      : May 09, 2021
|
| For any query and suggestion please contact at info@brotecs.com
|
'''
# user class used to store all the personal information of bank account holders and it used as a base class for Bank class
class user:
    # Fuction acts as constructor
    # Input parameters: name -> String, age->Integer, gender->String
    # Return parameter: void
    # Additional Details:  N/A
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # Function to display personal information
    # Input parameter: self
    # Return parameter: void 
    def displayPersonalInfo(self):
        print("****************Personal Information********************")
        print(f"              Name: {self.name}\n              Age : {self.age}\n              gender: {self.gender}\n\n")


# Bank class used to provide all the functionality for account holders and it is derived class of ue=rer class
class Bank (user):
    # Fuction acts as constructor
    # Input parameters: name -> String, age->Integer, gender->String
    # Return parameter: void
    # Additional Details:  N/A
    def __init__(self, name, age, gender):
        #
        super().__init__(name, age, gender)
        # This variable intiallize every account holders balance as zero by default
        self.__balance = 0

    # Function to deposit money to the bank
    # Input parameter: amount->Integer
    # Return parameter: void
    # Additional detaila: N/A
    def depositMoney(self,amount):
        self.amount = amount
        self.__balance  = self.amount + self.__balance
        print(f"Hi {self.name} ${self.amount} added to your account successfully. New Balance: ${self.__balance} ")

    # Function to withdraw money from the bank
    # Input parameter: amount->Integer
    # Return parameter: void
    # Additional detaila: N/A    
    def withdrawMoney(self,amount):
        self.amount = amount
        if self.amount > self.__balance:
            print(f"Insufficient balance! Your current balance is : ${self.__balance}\n\n")
        else:
            self.__balance = self.__balance - self.amount
            print(f"Hi {self.name} Withdraw of ${self.amount} is successful. Current balance : ${self.__balance}\n\n") 

    # Function to check account holders balance
    # Input parameter: void
    # Return parameter: void
    # Additional detaila: N/A
    def checkBalance(self):
        print(f"Dear {self.name}. Your current balance is ${self.__balance}\n\n")


print("\n*************************Welcome to BBank*************************\n")
# Prompt user to input his/her name
name = input("Enter your Name: ")
# Prompt user to input his/her age
age = input("Your age: ")
# Prompt user to input his/her name
gender  = input("Your Gender: ")
#Instantiation of class by creating an object of Bank class and passing name, age, gender as agruments.
userOne = Bank(name, age, gender)
print(f"Congratulations! {name} ! Account creation Successfull\n")

while(True):
    # provide menu option to users
    print(f'Dear {name}, Please choose from below option\n \n')
    choice = input(" 1.See Account Information\n 2.Withdraw Money\n 3.Diposit Money\n 4.Check balance\n 5.Exit \n\n")
    if(choice == '1'):
        # Displaying userinformation
        userOne.displayPersonalInfo()
    elif(choice == '2'):
        # Prompting user for the amount of money they want to withdraw from their account
        withdrawAmount = int(input("Enter amount to withdraw : $"))
        userOne.withdrawMoney(withdrawAmount)
    elif(choice == '3'):
         # Prompting user for the amount of money they want to deposit from their account
        depositAmount = int(input("Enter amount to deposit : $"))
        userOne.depositMoney(depositAmount)
    elif choice== '4':
        # Showing balance to the user
        userOne.checkBalance()
    elif choice =='5':
        # Exit from the system
        break
    else: 
        # Showing user the Error message for choosing wrong option from Menu
        print(f'Wrong choice {name} : please choose from the menu')
