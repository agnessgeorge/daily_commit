# Object Oriented Programming Challenge

# For this challenge, create a bank account class that has two attributes:
#* owner
#* balance

#and two methods:

#* deposit
#* withdraw

#As an added requirement, withdrawals may not exceed the available balance.
#Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:
       
    deposits = 0
    withdraws = 0
 

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance


    def __str__(self):
        print str(self.__class__) + ": " + str(self.__dict__)


    def deposit(self,depos):
        self.depos = depos
        self.deposits = deposits
        self.deposits = self.deposits + self.depos
        print("you deposited %d "%depos)
        print("your total deposits is %d \n"%deposits)
        

    def withdraw(self,withd):
        self.withd = withd
        self.withdraws = withdraws
        self.withdraws = self.withdraws + self.withd
        print("you withdrew %d "%withd)
        print("you total withdraws is %d \n"%withdraws)



# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
acct1.owner

# 4. Show the account balance attribute
acct1.balance

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)