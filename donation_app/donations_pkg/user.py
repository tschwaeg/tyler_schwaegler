def login(database, username, password):
    if username in database.keys() and database[username] == password:
        print("Welcome", username + "!\n")
        return username 
    elif username in database.keys() and database[username] != password:
        print ("Invalid password for", username)
        return ""
    else:
        print("Username not found.")

def register(database, username):
    if username in database.keys():
        print("Username already registered.")
        return ""
    else:
        print("Username", username, "has been registered.")
        return username 