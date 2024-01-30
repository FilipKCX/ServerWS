import sqlite3
from datetime import datetime 

def createUser(email, password, isUser): #createUser name email password
  print("START CREATE USER")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()

  cursor.execute("SELECT max(uID) FROM users")
  uID = cursor.fetchone()
  
  #print(uID)
  print(isUser)

  if uID[0] == None: 
    uID = 1
  else:
    uID = uID[0] + 1
    #print(uID)
  '''
  print("START CREATING CARDS")
    #-----------------------------------------------------------------------------------------------------------------------------
  if isUser == "0":
    cursor.execute("SELECT uID FROM users WHERE isUser = 1")
    userIDs = cursor.fetchall()
    
    print("userIDs: " + str(userIDs))

    cursor.execute("SELECT max(likeID) FROM likesCard")
    likeID = cursor.fetchone()

    print(likeID)

    if likeID[0] == None: 
      likeID = 1
    else:
      likeID = likeID[0] + 1

    if userIDs != None:
      for userID in userIDs:
        cursor.execute("INSERT INTO likesCard (likeID, userID, likerID, isLiked) VALUES (?, ?, ?, 0)", (str(likeID), str(userID), str(uID)))
        likeID += 1
        print(likeID)
  elif isUser == "1":
    cursor.execute("SELECT uID FROM users WHERE isUser = 0")
    userIDs = cursor.fetchall()

    print("userIDs: " + str(userIDs))

    cursor.execute("SELECT max(likeID) FROM likesCard")
    likeID = cursor.fetchone()

    print(likeID)

    if likeID[0] == None: 
      likeID = 1
    else:
      likeID = likeID[0] + 1

    if userIDs != None:
      for userID in userIDs:
        cursor.execute("INSERT INTO likesCard (likeID, userID, likerID, isLiked) VALUES (?, ?, ?, 0)", (str(likeID), str(userID), str(uID)))
        likeID += 1
        print(str(likeID))
    #------------------------------------------------------------------------------------------------------------------------------
  print("END CREATING CARDS")
  '''
  cursor.execute("INSERT INTO users (uID, email, password, isUser) VALUES (?, ?, ?, ?)", (uID, email, password, isUser))
  connection.commit()
  connection.close()
  print("END CREATE USER")
  return uID

def createChat(email, password, isUser): #createUser name email password
  print("START CREATE USER")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  cursor.execute("SELECT max(uID) FROM users")
  uID = cursor.fetchone()
  #print(uID)
  if uID[0] == None: 
    uID = 1
  else:
    uID = uID[0] + 1
    #print(uID)

  cursor.execute("INSERT INTO users (uID, email, password, isUser) VALUES (?, ?, ?, ?)", (uID, email, password, isUser))
  connection.commit()
  connection.close()
  print("END CREATE USER")
  return uID

def createUserProfile(uID, name, email, telefon, abschluss, studium, semester, berufserf, skills, profilb, werdeg, Stunden , logo):
  print("START CREATE USERPROFILE")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  print(logo)
  cursor.execute("DELETE FROM UserProfile WHERE uID = ?" , (uID,))
  cursor.execute("INSERT INTO userProfile (uID, name, email, telefon, abschluss, studium, semester, berufserf, skills, profilb, werdeg, Stunden , logo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? , ?, ?, ?, ?)", (uID, name, email, telefon, abschluss, studium, semester, berufserf, skills, profilb, werdeg, Stunden , logo))
  connection.commit()
  connection.close()
  print("END CREATE USER")
  return 1

def createCompanyProfile(uID, name, email, Standort , wersw, waswb, karriere, geschichte, logo):
  print("START CREATE USERPROFILE")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  print(logo)
  cursor.execute("DELETE FROM CompanyProfile WHERE uID = ?" , (uID,))
  cursor.execute("INSERT INTO CompanyProfile (uID, name, email, Standort , wersw, waswb, karriere, geschichte, logo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? )", (uID, name, email, Standort , wersw, waswb, karriere, geschichte, logo))
  connection.commit()
  connection.close()
  print("END CREATE USER")
  return 1

def addLike (uID, cID):
  print("START ADDLIKE")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  cursor.execute('DELETE FROM Like WHERE uID = ? AND cID = ?', (uID, cID))
  cursor.execute("INSERT INTO Like (uID, cID) VALUES (?,?)", (uID,cID))
  connection.commit()
  connection.close()
  return 1

def addAlreadyLike (uID, cID):
  print("START AlreadyLiked")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  cursor.execute('DELETE FROM AlreadyLike WHERE uID = ? AND cID = ?', (uID, cID))
  cursor.execute("INSERT INTO AlreadyLike (uID, cID) VALUES (?,?)", (uID,cID))
  connection.commit()
  connection.close()
  return 1

def setTage (uID, mo, di, mi, do, fr):
  print("START setTage")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  cursor.execute('DELETE FROM Tage WHERE uID = ?', (uID,))
  cursor.execute("INSERT INTO Tage (uID, mo, di, mi, do, fr) VALUES (?,?,?,?,?,?)", (uID, mo, di, mi, do, fr))
  connection.commit()
  connection.close()
  return 1

def addMessagee (chatID, sID, content):
  print("START ADDLIKE")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  cursor.execute("SELECT max(messageID) FROM messagee")
  current_datetime = datetime.now()

    # Format the datetime as a string without seconds
  timestamp = current_datetime.strftime("%d.%m.%Y %H:%M")
  print(timestamp)
  maxID = cursor.fetchone()[0]
  if maxID == None:
    maxID = 1
  else:
    maxID += 1
  cursor.execute("INSERT INTO messagee (chatID, sID, content, messageID, time) VALUES (?,?,?,?,?)", (chatID, sID, content, maxID, timestamp))
  connection.commit()
  connection.close()
  return 1

def deleteLikes (uID, cID):
  print("START ADDLIKE")
  connection = sqlite3.connect('main.db')
  print
  cursor = connection.cursor()
  cursor.execute('DELETE FROM Like WHERE uID = ? AND cID = ?', (uID, cID))
  connection.commit()
  connection.close()
  return 10

def addChats (uID, cID):
  print("START Add chats")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  cursor.execute("SELECT chatID FROM Chat WHERE uID = ? AND cID = ?", (uID, cID))
  chatID = cursor.fetchone()
  print(chatID)
  if chatID == None:
    cursor.execute("SELECT max(chatID) FROM Chat")
    maxchatID = cursor.fetchone()[0]
    if maxchatID == None:
      chatID = 1
    else:
      chatID = maxchatID + 1
  else:
    chatID = chatID[0]

  cursor.execute("INSERT INTO Chat (chatID, uID, cID) VALUES (?,?,?)", (chatID,uID,cID))
  connection.commit()
  connection.close()
  return 1

'''cursor.execute(CREATE TABLE message (
                  messageID INTEGER,
                  SendID INTEGER,
                  RecvID INTEGER,
                  Content INTEGER,
                  timestamp TEXT
                 ))'''

def createMessage(SendID, RecvID, Content): #createMessage Sneder Empfänger Inhalt
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()

  cursor.execute("SELECT chatID FROM message WHERE (SendID = ? AND RecvID = ?) OR (SendID = ? AND RecvID = ?)", (SendID, RecvID, RecvID, SendID))
  chatID = cursor.fetchone()
  print(chatID)
  if chatID == None:
    cursor.execute("SELECT max(chatID) FROM message")
    maxchatID = cursor.fetchone()[0]
    if maxchatID == None:
      chatID = 1
    else:
      chatID = maxchatID + 1
  else:
    chatID = chatID[0]

  cursor.execute("SELECT max(messageID) FROM message")
  maxID = cursor.fetchone()[0]

  if maxID == None:
    maxID = 1
  else:
    maxID += 1

  cursor.execute("INSERT INTO message (chatID, messageID, SendID, RecvID, Content) VALUES (?, ?, ?, ?, ?)", (chatID, maxID, SendID, RecvID, Content))

  connection.commit()
  connection.close()

  return maxID, chatID

'''
print("-------------------------------------------------")
print(createMessage("3", "1", "das hier ist eine neue Nachricht"))
#'''


def updateLiked(userID, likerID):
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()

  cursor.execute("UPDATE likesCard SET isLiked = 1 WHERE userID = ? AND likerID = ?", (str(userID), str(likerID)))

  connection.commit()
  connection.close()

def createLikesCardWithUser(userID):
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()

  cursor.execute("SELECT uID FROM users WHERE isUser = 1")
  companyIDs = cursor.fetchone()

  connection.close()

  for companyID in companyIDs:
    createLikeCard(userID, companyID)

def createLikesCardWithCompany(companyID):
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()

  cursor.execute("SELECT uID FROM users WHERE isUser = 0")
  userIDs = cursor.fetchone()

  for userID in userIDs:
    cursor.execute("SELECT max(likeID) FROM likesCard")
    likeID = cursor.fetchone()
    print(likeID)
    if likeID[0] == None: 
      likeID = 1
    else:
      likeID = likeID[0] + 1

def createLikeCard(userID, CompanyID):
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()

  cursor.execute("SELECT max(likeID) FROM likesCard")
  likeID = cursor.fetchone()
  print(likeID)
  if likeID[0] == None: 
    likeID = 1
  else:
    likeID = likeID[0] + 1

  print(likeID)

  cursor.execute("INSERT INTO likesCard (likeID, userID, likerID, isLiked) VALUES (?, ?, ?, 0)", (str(likeID), str(userID), str(CompanyID)))
  connection.commit()
  connection.close()

  return likeID

def addToLikedTable(userID, CompanyID):
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()

  cursor.execute("INSERT INTO likesCard (likeID, userID, likerID, isLiked) VALUES (0, ?, ?, 0)", (str(userID), str(CompanyID)))

  connection.commit()
  connection.close()

#print(createLikeCard("1", "2"))

#print(createUser("sada", "sadasd", "1"))