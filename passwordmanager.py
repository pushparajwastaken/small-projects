import sqlite3
conn=sqlite3.connect('passwords.db')
pointer=conn.cursor()
pointer.execute('''
CREATE TABLE IF NOT EXISTS apps(
                id INTEGER PRIMARY KEY,
                app TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL -- Changed INTEGER to TEXT
                )
''')
def listpasswords():
       pointer.execute("SELECT * FROM apps")
       for rows in pointer.fetchall():
              print(rows)
def addpasswords(appname,username,password):
       pointer.execute("INSERT INTO apps(app,username,password) VALUES(?,?,?)",(appname, username, password))
       conn.commit()
def updatepassword(appsid,newappname,newusername,newpassword):
       pointer.execute("UPDATE  apps set app= ?, username= ?,password=? where id=?", (newappname,newusername,newpassword,appsid))
       conn.commit()
def deletepasswords(appid):
       pointer.execute("DELETE FROM apps where id = ?", (appid,))
       conn.commit()
def main():
    while True:
        print("\n Welcome to the Password Manager App\n")
        print("1. List all Passwords")
        print("2. Add Password")
        print("3. Update Password or username")
        print("4. Delete the password")
        print("5. Quit")
        choice=int(input("Enter your Choice: "))
        if choice==1:
                listpasswords()
        elif choice==2:
                appname=input("Enter the app name: ")
                username=input("Enter your username:")
                password=input("Enter the Password: ")
                addpasswords(appname, username,password)
        elif choice==3:
                appsid=int(input("Enter the ID: "))
                newappname=input("Enter the App name: ")
                newusername=input("Enter the Username: ")
                newpassword=input("Enter the Password")
                updatepassword("appsid, newappname, newusername, newpassword")
        elif choice==4:
                appsid=int(input("Enter the ID you want to delete: "))
                deletepasswords(appsid)
        elif choice==5:
                break
        else :
                print("Invalid Input")
    


    
if __name__=="__main__":
    main()
conn.close()