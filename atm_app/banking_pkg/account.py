def show_balance(balance):
    print("Current Balance: $" + str(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return balance + float(amount)

def withdrawal(balance):
    while True:
        amount = input("\nEnter the amount to withdraw: ")
        if amount == "cancel" or amount == "c":
            print("Returning you to the main screen...")
            return balance
        if float(amount) > balance:
            print("\nAmount requested to withdraw exceeds account balance. Please enter an amount equal to or less than your account balance. To cancel your withdrawal request, enter 'cancel'\n")
            continue
        if float(amount) <= balance:
            return balance - float(amount)
def logout(name):
    print("Goodbye", name + "!")