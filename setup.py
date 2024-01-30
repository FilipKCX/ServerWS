import sqlite3

connection = sqlite3.connect('main.db')
cursor = connection.cursor() #fuer befehle
#cursor.execute('''DROP TABLE IF EXISTS message''')
#cursor.execute('''DROP TABLE IF EXISTS users''')
#cursor.execute('''DROP TABLE IF EXISTS likesCard''')

#USERS
cursor.execute('''CREATE TABLE users (
                    uID INTEGER,
                    username TEXT,
                    email TEXT,
                    password TEXT,
                    isUser INTEGER
                    
                 )''')

connection.commit()
connection.close()


'''
immer 2 userIDs --> welcher userID

messeageID
usenderID --> userId
chatID


-------------------
return [[m12, m22 , 23e2 ],[]]


'''

'''CREATE TABLE CompanyProfile (
                     uID INTEGER,
                     name TEXT,
                     email TEXT,
                     Standort TEXT,
                     wersw TEXT,
                     waswb TEXT,
                     karriere TEXT,
                     geschichte TEXT,
                     logo TEXT

               
                    cID
                 )'''