from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"Admin": "password123"}
donations = []
authorized_user = ""

while True:
    show_homepage()

    if authorized_user == "":
        print("Please log-in or register to donate.")
    else:
        print("\nLogged in as:", authorized_user)

    choice = input("\nPlease choose an option to continue: ")
    print("\n")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter Password: ")
        authorized_user = login(database, username, password)
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username != "":
            authorized_user = register(database, username)
            database[username] = password
        if username == "":
            print("Username cannot be blank. Returning you to the Homepage.")
    elif choice == "3":
        if authorized_user == "":
            print("You are not logged in!")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
    elif choice == "4":
        show_donations(donations)
    elif choice == "5":
        print("You have chosen to exit, goodbye for now!")
        break
    else:
        print("Invalid entry, please try again.")

print(database) #verification of ending dictionary with users
print(donations) #verification of ending list of donations

