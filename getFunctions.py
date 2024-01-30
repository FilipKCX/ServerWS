import sqlite3
import datetime

def getLoginUser(email, password):
    print("START getLoginUser")
    print(email)
    print(password)
    connection = sqlite3.connect('main.db')
    cursor = connection.cursor()

    cursor.execute("SELECT uID FROM users WHERE email = ? AND password = ?", (email, password))
    uID = cursor.fetchone()

    if uID == None:
        uID = "a"
    else:
        uID = uID[0]

    connection.close()
    print("END getLoginUser")
    return uID


def getIsUser(usID):
  print("START getIsUser")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  cursor.execute("SELECT isUser FROM users WHERE uID = ?", (usID,))
  isUser = cursor.fetchone()
  connection.close()
  print(isUser)
  print("END getIsUser")
  return isUser[0]


def getProfileInfox(uID):
  print("START getProfileInfox")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  cursor.execute("SELECT uID, name, studium, abschluss, Stunden, berufserf, logo FROM UserProfile WHERE uID = ?", (uID,))
  print(uID)
  name = cursor.fetchall()
  print(name)
  connection.close()
  return name

def getProfileInfoxx(uID):
  print("START getProfileInfox")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  cursor.execute("SELECT name FROM UserProfile WHERE uID = ?", (uID,))
  print(uID)
  name = cursor.fetchall()
  print(name)
  connection.close()
  return name

def getProfileInfo(uID):
  print("START getProfileInfo")
  connection = sqlite3.connect('main.db')
  cursor = connection.cursor()
  cursor.execute("SELECT uID, name, email, telefon, abschluss, studium, semester, berufserf, skills, profilb, werdeg, Stunden , logo FROM UserProfile WHERE uID = ?", (uID,))
  print(uID)
  name = cursor.fetchall()
  print(name)
  connection.close()
  return name

def getUsers():
   print("Start getUSers")
   connection = sqlite3.connect('main.db')
   cursor = connection.cursor()
   cursor.execute("SELECT uID from UserProfile")
   names = cursor.fetchall()  
   names = [item[0] for item in names]
   print(names)
   return names

def getLikes(uID):
   print("START getLikes")
   connection = sqlite3.connect('main.db')
   cursor = connection.cursor()
   cursor.execute("SELECT cID FROM Like WHERE uID=" + uID ) 
   likes = cursor.fetchall()
   
   if not likes:
          return None
   likes = [item[0] for item in likes]
   print(likes)
   return likes

'''
def getChats(uID):
   print("START getChats")
   connection = sqlite3.connect('main.db')
   cursor = connection.cursor()
   cursor.execute("SELECT cID FROM Chats WHERE uID=" + uID ) 
   likes = cursor.fetchall()   
   if not likes:
          return None
   likes = [item[0] for item in likes]
   print(likes)
   return likes
#'''


def getCompanyInfox(uID):
   print("START CompX")
   connection = sqlite3.connect('main.db')
   cursor = connection.cursor()
   cursor.execute("SELECT name, logo FROM CompanyProfile WHERE uID = ?", (uID,))
   print(uID)
   info = cursor.fetchall()
   print(info)
   connection.close()
   return info

def getCompanyInfos(uID):
   print("START getProfileInfo")
   connection = sqlite3.connect('main.db')
   cursor = connection.cursor()
   cursor.execute("SELECT uID, name, email, Standort , wersw, waswb, karriere, geschichte, logo FROM CompanyProfile WHERE uID = ?", (uID,))
   print(uID)
   infos = cursor.fetchall()
   print(infos)
   connection.close()
   return infos

def getTage(uID):
   print("START getTage")
   connection = sqlite3.connect('main.db')
   cursor = connection.cursor()
   cursor.execute("SELECT mo, di, mi, do, fr FROM Tage WHERE uID = ?", (uID,))
   print(uID)
   tage = cursor.fetchall()
   print(tage)
   connection.close()
   return tage


def getMessageWithMessageID(messageID):
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()

   cursor.execute("Select * FROM message WHERE messageID = ?", (str(messageID)))
   message = cursor.fetchone()

   connection.close()

   return message

def getallChats(userID):
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()
   print(userID)
   cursor.execute("SELECT DISTINCT chatID FROM message WHERE SendID = ? OR RecvID = ?", (userID, userID))
   allchatIDs = cursor.fetchall()

   allChats = []

   for chatID in allchatIDs:
      cursor.execute("SELECT * FROM message WHERE chatID = ?", (str(chatID[0])))
      allChats.append(cursor.fetchall())

   connection.commit()
   print(allChats)
   return allChats

def getChats(userID):
   print("get CHATSSS")
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()

   cursor.execute("SELECT DISTINCT cID, chatID  FROM Chat WHERE uID = ? ", (userID,))
   allchats = cursor.fetchall()
   print(allchats)
   if not allchats:
          return None
   print(allchats)
   return allchats

def getChatsC(userID):
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()

   cursor.execute("SELECT DISTINCT uID, chatID  FROM Chat WHERE cID = ? ", (userID,))
   allchatIDs = cursor.fetchall()

   if not allchatIDs:
          return None
   print(allchatIDs)
   return allchatIDs

def getMessages(chatID):
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()

   cursor.execute("SELECT * FROM messagee WHERE chatID = ?", (chatID,))
   allmessages = cursor.fetchall()
   if not allmessages:
          return None
   print(allmessages)
   return allmessages



def getChatsId(userID):
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()

   cursor.execute("SELECT DISTINCT chatID FROM message WHERE SendID = ? OR RecvID = ?", (userID, userID))
   allchatIDs = cursor.fetchall()

   if not allchatIDs:
          return None
   allchatIDs = [item[0] for item in allchatIDs]
   print(allchatIDs)
   return allchatIDs
   
def getAlreadyLiked(userID):
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()

   cursor.execute("SELECT DISTINCT uID FROM AlreadyLike WHERE cID = ?", (userID,))
   allchatIDs = cursor.fetchall()

   if not allchatIDs:
          return None
   allchatIDs = [item[0] for item in allchatIDs]
   print(allchatIDs)
   return allchatIDs

def getChatUpdate(chatID, maxMessageID):
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()

   cursor.execute("SELECT * FROM message WHERE messageID > ? AND chatID = ?", (str(maxMessageID), str(chatID)))
   newChatPart = cursor.fetchall()

   connection.close()

   return newChatPart


def getAllChatUpdates(messageIDArray):
   newChatParts = []

   for messages in messageIDArray:
      newChatParts.append(getChatUpdate(messages[0], messages[1]))

   return newChatParts




'''
print("-------------------------------------------------")
print(updateChat(1, 7))
print("-----------------")
print(updateChat(1, 6))
#'''

#print(getallChats(1))


def getLikeCardByID(LikeID):
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()

   cursor.execute("SELECT * FROM likesCard WHERE likeID = ?", (str(LikeID)))
   LikeCard = cursor.fetchone()

   connection.close()
   return LikeCard

def getAllLikeCardsByUserCompanyID(CompanyID):
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()

   cursor.execute("SELECT * FROM likesCard WHERE likerID = ? AND isLiked = 0", (str(CompanyID),))
   LikeCards = cursor.fetchall()

   return LikeCards

def getLikedUser(CompanyID): #getLikedUser CompanyID
   connection = sqlite3.connect("main.db")
   cursor = connection.cursor()

   cursor.execute("SELECT userID FROM likesCard WHERE likerID = ?", (str(CompanyID),))
   LikeCards = cursor.fetchall()

   connection.close()
   return LikeCards


#print(getAllLikeCardsByUserCompanyID("1", "2"))
#print(getAllLikeCardsByUserCompanyID(166))