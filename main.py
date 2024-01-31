import socket
import requests
import threading
import gzip
import json
import setFunctions
import getFunctions


HOST = "localhost"
PORT = 34123    


def handle_http_request(socket, data):
    lines = data.decode().split('\n')
    #print(lines)
    request_line = lines[0]
    print(request_line)
    method, url, version = request_line.split(' ')
    print(method)
    print(version)
    print(url)
    url = url.replace('/', '')
    url = url.replace("%20", ' ')
    url = url.replace("%C3%B6", 'ö')
    url = url.replace("%C3%9F", 'ß')
    url = url.replace("%C3%A4", 'ä')
    url = url.replace("%C3%BC", 'ü')
    url2 = url.split('&')   
    print(url2)



    
    Task = url2[0]

    if Task == "createUser": #createUser name password
        uID = setFunctions.createUser(url2[1], url2[2], url2[3])
        print(uID)
        Response = create_http_response(200, str(uID))
        print(Response)
        socket.sendall(Response)
        socket.close()

    elif Task == "getLoginUser": #getLoginUser name password
        uID = getFunctions.getLoginUser(url2[1], url2[2])
        print(uID)
        Response = create_http_response(200, str(uID))
        print(Response)
        socket.sendall(Response)
        socket.close()

    elif Task == "getIsUser":
        isUser = getFunctions.getIsUser(url2[1])
        Response = create_http_response(200, str(isUser))
        socket.sendall(Response)
        socket.close()

    elif Task == "createProfile":
        bild = url2[13]
        bild = bild
        sID = setFunctions.createUserProfile(url2[1],url2[2],url2[3],url2[4],url2[5],url2[6],url2[7],url2[8],url2[9],url2[10],url2[11],url2[12], bild)
        Response = create_http_response(200, str(sID))
        socket.sendall(Response)
        socket.close()

    elif Task == "getProfileInfo":
        print("Hier ist das WICHTIGE hhhhhh" + url2[1])
        name = getFunctions.getProfileInfo(url2[1])
        Response = create_http_response(200, json.dumps(name))
        socket.sendall(Response)
        socket.close()

    elif Task == "getProfileInfox":
        print("Hier ist das WICHTIGE" + url2[1])
        name = getFunctions.getProfileInfox(url2[1])
        Response = create_http_response(200, json.dumps(name))
        socket.sendall(Response)
        socket.close()
    
    elif Task == "getProfileInfoxx":
        print("Hier ist das WICHTIGE" + url2[1])
        name = getFunctions.getProfileInfoxx(url2[1])
        Response = create_http_response(200, json.dumps(name))
        socket.sendall(Response)
        socket.close()

    elif Task == "getUsers":
        names = getFunctions.getUsers()
        Response = create_http_response(200, str(names))
        socket.sendall(Response)
        socket.close()

    elif Task == "addLike":
        names = setFunctions.addLike(url2[1], url2[2])
        Response = create_http_response(200, str(names))
        socket.sendall(Response)
        socket.close()
    
    elif Task == "alreadyLiked":
        names = setFunctions.addAlreadyLike(url2[1], url2[2])
        Response = create_http_response(200, str(names))
        socket.sendall(Response)
        socket.close()
        
    elif Task == "deleteLike":
        names = setFunctions.deleteLikes(url2[1], url2[2])
        Response = create_http_response(200, str(names))
        socket.sendall(Response)
        socket.close()

    elif Task == "addChats":
        names = setFunctions.addChats(url2[1], url2[2])
        Response = create_http_response(200, str(names))
        socket.sendall(Response)
        socket.close()

    elif Task == "createMessagee":
        names = setFunctions.addMessagee(url2[1], url2[2],url2[3])
        Response = create_http_response(200, str(names))
        socket.sendall(Response)
        socket.close()

    elif Task == "getLikes":
        likes = getFunctions.getLikes(url2[1])
        Response = create_http_response(200, str(likes))
        socket.sendall(Response)
        socket.close()

    elif Task == "getChats":
        likes = getFunctions.getChats(url2[1])
        Response = create_http_response(200, json.dumps(likes))
        socket.sendall(Response)
        socket.close()

    elif Task == "getChatsC":
        likes = getFunctions.getChatsC(url2[1])
        Response = create_http_response(200, json.dumps(likes))
        socket.sendall(Response)
        socket.close()
    
    elif Task == "getMessages":
        likes = getFunctions.getMessages(url2[1])
        Response = create_http_response(200, json.dumps(likes))
        socket.sendall(Response)
        socket.close()
    
    elif Task == "getChatsId":
        likes = getFunctions.getChatsId(url2[1])
        Response = create_http_response(200, str(likes))
        socket.sendall(Response)
        socket.close()
    
    elif Task == "getAlreadyLiked":
        likes = getFunctions.getAlreadyLiked(url2[1])
        Response = create_http_response(200, str(likes))
        socket.sendall(Response)
        socket.close()
        
    elif Task == "createCompanyProfile":
        bild = url2[8]
        bild = bild
        likes = setFunctions.createCompanyProfile(url2[1],url2[2],url2[3],url2[4],url2[5],url2[6],url2[7],url2[8], url2[9])
        Response = create_http_response(200, str(likes))
        socket.sendall(Response)
        socket.close()
    
    elif Task == "setTage":
        likes = setFunctions.setTage(url2[1],url2[2],url2[3],url2[4],url2[5],url2[6])
        Response = create_http_response(200, str(likes))
        socket.sendall(Response)
        socket.close()

    elif Task == "getTage":
        likes = getFunctions.getTage(url2[1])
        Response = create_http_response(200, json.dumps(likes))
        socket.sendall(Response)
        socket.close()

    elif Task == "getCompanyInfox":
        infox = getFunctions.getCompanyInfox(url2[1])
        Response = create_http_response(200, json.dumps(infox))
        socket.sendall(Response)
        socket.close()

    elif Task == "getCompanyInfos":
        infox = getFunctions.getCompanyInfos(url2[1])
        Response = create_http_response(200, json.dumps(infox))
        socket.sendall(Response)
        socket.close()

    elif Task == "getLikedUser": #getLikedUser CompanyID
        UserArray = getFunctions.getLikedUser(url2[1])
        Response = create_http_response(200, str(UserArray))
        socket.sendall(Response)
        socket.close()

    elif Task == "createMessage": #createMessage Sender Empfänger Inhalt
        chatID = setFunctions.createMessage(url2[1], url2[2], url2[3])
        Response = create_http_response(200, str(chatID))
        socket.sendall(Response)
        socket.close()

    elif Task == "createMessagee": #createMessage Sender Empfänger Inhalt
        chatID = setFunctions.createMessage(url2[1], url2[2], url2[3])
        Response = create_http_response(200, str(chatID))
        socket.sendall(Response)
        socket.close()

    elif Task == "getallChats": #getallChats userID
        allChats = getFunctions.getallChats(url2[1])
        Response = create_http_response(200, str(allChats))
        print(allChats)
        socket.sendall(Response)
        socket.close()

    elif Task == "getChats": #getallChats userID
        allChats = getFunctions.getChats(url2[1])
        Response = create_http_response(200, str(allChats))
        print(allChats)
        socket.sendall(Response)
        socket.close()
    
    
    


'''
def create_http_response(status_code, content):
    response = f"HTTP/1.1 {status_code}\r\nContent-Length: {len(content)}\r\n\r\n{content}"
    return response.encode()
'''

def create_http_response(status_code, content):
    headers = "HTTP/1.1 {status_code}\r\nContent-Length: {content_length}\r\nAccess-Control-Allow-Origin: *\r\n\r\n".format(
        status_code=status_code,
        content_length=len(content)
    )
    response = headers + content
    return response.encode()









def main():
    

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    server_socket.bind((HOST, PORT))


    server_socket.listen()

    print("polling...")

    while True:


        client_socket, _ = server_socket.accept()
        print("connected")
        data = client_socket.recv(1024)
        print(data)
        # Verarbeite die HTTP-Anfrage        
        task = threading.Thread(target=handle_http_request, args=(client_socket, data))
        task.start()

        #if client_socket is not None:
        #    client_socket.close()

main()
