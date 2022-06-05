from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("\nUser: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("          === Automated Teller Machine ===          ")

balance = 0

while True: 
    name = input("Enter name to register: ")
    if len(name) not in range(1, 11):
        print("Invaild name. Your name must be between 1 and 10 characters in length. Please try again.")
        continue
    else:
        break
while True:
    pin = input("Enter PIN: ")
    if len(pin) != 4:
        print("Invalid PIN. Your PIN must be 4 characters in length. Please try again.")
        continue
    else:
        break
while True:
    zz = 3 #sets the stop of the range below depending on how many tries you want to give the user to try and enter a promo code before it forces them to continue. 
    xx = zz - 1 #sets the conditionals for the if statements below in respect to the stop of the range. 
    for i in range(0, zz, 1): 
        promo_code = input("Do you have a promo code? If you do not, enter 'no': ")
        promo_code = promo_code.lower()
        if promo_code == "bonus25":
            balance = 25
            print("\nPromo code accepted. You received a $25 bonus for opening this account.")
            break
        if promo_code == "bonus50":
            balance = 50 
            print("\nPromo code accepted. You received a $50 bonus for opening this account.")
            break
        if promo_code == "no":
            break
        if i < xx:
            i += 1
            print("Invalid promo code. Try again. You have", str((zz - i)), "tries remaining.")
            continue
        if i == xx:
            print("Invalid promo code. You have", str((xx - i)), "tries remaining. Please proceed to the next phase of registration.")
            continue
    break

print("\nSuccess!", name, "has been registered with a PIN of", pin, "and a starting balance of $" + str(balance) + "\n")

print("          === Automated Teller Machine ===          ")
print("LOGIN")
while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name == name_to_validate and pin == pin_to_validate:
        print("Login successful!")
        break
    elif name != name_to_validate or pin != pin_to_validate:
        print("Invalid Credentials!")

while True:
    atm_menu(name)
    option = input("\nChoose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdrawal(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
    else:
        print("Invalid entry. Please try again")
    

