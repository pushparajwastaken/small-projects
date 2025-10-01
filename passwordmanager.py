import sqlite3
import random
import string

# Database connection
conn = sqlite3.connect('passwords.db')
pointer = conn.cursor()
pointer.execute('''
CREATE TABLE IF NOT EXISTS apps(
                id INTEGER PRIMARY KEY,
                app TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
                )
''')

# List all stored passwords
def listpasswords():
    pointer.execute("SELECT * FROM apps")
    for row in pointer.fetchall():
        print(row)

# Add a new password
def addpasswords(appname, username, password):
    pointer.execute("INSERT INTO apps(app, username, password) VALUES(?,?,?)", (appname, username, password))
    conn.commit()

# Update existing password
def updatepassword(appsid, newappname, newusername, newpassword):
    pointer.execute("UPDATE apps SET app = ?, username = ?, password = ? WHERE id = ?", (newappname, newusername, newpassword, appsid))
    conn.commit()

# Delete a password
def deletepasswords(appsid):
    pointer.execute("DELETE FROM apps WHERE id = ?", (appsid,))
    conn.commit()

# Search for passwords by app name
def searchpasswords(appname):
    pointer.execute("SELECT * FROM apps WHERE app LIKE ?", (f"%{appname}%",))
    results = pointer.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print(f"No results found for app name: {appname}")

# Generate a strong random password
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Main Programme
def main():
    while True:
        print("\n Welcome to the Password Manager App\n")
        print("1. List all Passwords")
        print("2. Add Password")
        print("3. Update Password or Username")
        print("4. Delete Password")
        print("5. Search Passwords by App Name")
        print("6. Generate a Random Password")
        print("7. Quit")
        choice = int(input("Enter your Choice: "))
        
        if choice == 1:
            listpasswords()
        elif choice == 2:
            appname = input("Enter the app name: ")
            username = input("Enter your username: ")
            password = input("Enter the password (or type 'generate' to create a random one): ")
            if password.lower() == 'generate':
                password = generate_password()
                print(f"Generated Password: {password}")
            addpasswords(appname, username, password)
        elif choice == 3:
            appsid = int(input("Enter the ID: "))
            newappname = input("Enter the App name: ")
            newusername = input("Enter the Username: ")
            newpassword = input("Enter the Password: ")
            updatepassword(appsid, newappname, newusername, newpassword)
        elif choice == 4:
            appsid = int(input("Enter the ID you want to delete: "))
            deletepasswords(appsid)
        elif choice == 5:
            appname = input("Enter the app name to search for: ")
            searchpasswords(appname)
        elif choice == 6:
            length = int(input("Enter the desired length of the password (default is 12): "))
            print(f"Generated Password: {generate_password(length)}")
        elif choice == 7:
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()

conn.close()
    main()

conn.close()

