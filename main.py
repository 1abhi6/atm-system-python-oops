class Atm:
    # Constructor
    def __init__(self):
        self.__pin = 0
        self.__currentBalance = 0

    # Create Pin

    def createPin(self):
        self.__pin = input("Enter your Pin: ")
        print("Pin created successfully")

    # Check Pin
    def checkPin(self):
        temp = input("Input your Pin: ")
        if temp == self.__pin:
            return True
        else:
            return False

    # Deposit money
    def depositMoney(self):
        check = self.checkPin()
        if check:
            self.balance = int(input("Enter the money you want to deposit: "))
            self.__currentBalance += self.balance
            print("Deposited successfully")
            print("Current Balance:", self.__currentBalance)
        else:
            print("Inalid Pin")

    # Withdraw money
    def withdrawMoney(self):
        check = self.checkPin()
        if check:
            withdrawAmount = int(input("Input the amount to withdraw: "))
            if withdrawAmount < self.__currentBalance:
                self.__currentBalance -= withdrawAmount
                print("Withdrawl Succesfully")
                print("Current Balance:", self.__currentBalance)
            else:
                print("Insufficent Funds!!!")
        else:
            print("Invalid Pin")

    # Check Balance
    def checkBalance(self):
        check = self.checkPin()
        if check:
            print("Current Balance:", self.__currentBalance)
        else:
            print("Invalid Input")

    # Check Pin getter function to get the pin
    def getPin(self):
        return self.__pin

    # Change pin setter function to set the pin
    def setPin(self, newPin):
        if newPin.isdigit():
            self.__pin = newPin
            print("Pin Changed Successfully!!!")
        else:
            print("Please check your pin again, It should be a number")


# *****-----End of the class Atm-----*****

# Creating the object
sbi = Atm()

# Creating the menu
while True:
    userInput = int(input("""
        Hello, How would you like to proceed?
        1. Create Pin
        2. Deposit
        3. Withdraw
        4. Check Balance
        5. Check Pin
        6. Change Pin
        7. Exit
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
        if (sbi.getPin() == 0):
            print("Please Create a Pin")
            sbi.createPin()
        else:
            print("Current Pin:", sbi.getPin())

    elif userInput == 6:
        check = sbi.checkPin()
        if check:
            newPin = input("Input new Pin: ")
            sbi.setPin(newPin)
        else:
            print("Invalid Pin")

    elif userInput == 7:
        break
    else:
        print("Invalid Input")
