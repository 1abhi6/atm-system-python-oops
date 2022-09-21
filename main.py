class Atm:
    # Constructor
    def __init__(self):
        self.pin = ""
        self.currentBalance = 0

    # Create Pin
    def createPin(self):
        self.pin = input("Enter your Pin: ")
        print("Pin created successfully")

    # Check Pin
    def checkPin(self):
        temp = input("Input your Pin: ")
        if temp == self.pin:
            return True
        else:
            return False

    # Deposit money
    def depositMoney(self):
        check = self.checkPin()
        if check:
            self.balance = int(input("Enter the money you want to deposit: "))
            self.currentBalance += self.balance
            print("Deposited successfully")
            print("Current Balance:", self.currentBalance)
        else:
            print("Inalid Pin")

    # Withdraw money
    def withdrawMoney(self):
        check = self.checkPin()
        if check:
            withdrawAmount = int(input("Input the amount to withdraw: "))
            if withdrawAmount < self.currentBalance:
                self.currentBalance -= withdrawAmount
                print("Withdrawl Succesfully")
                print("Current Balance:", self.currentBalance)
            else:
                print("Insufficent Funds!!!")
        else:
            print("Invalid Pin")

    # Check Balance
    def checkBalance(self):
        check = self.checkPin()
        if check:
            print("Current Balance:", self.currentBalance)
        else:
            print("Invalid Input")
# End of the class Atm


# Creating the object
sbi = Atm()

# Creating the menu
while True:
    userInput = int(input("""
        Hello, How would you like to proceed?
        1. Create pin
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Exit
    """))
    if userInput == 1:
        sbi.createPin()
    elif userInput == 2:
        sbi.depositMoney()
    elif userInput == 3:
        sbi.withdrawMoney()
    elif userInput == 4:
        sbi.checkBalance()
    elif userInput == 5:
        break
    else:
        print("Invalid Input")
