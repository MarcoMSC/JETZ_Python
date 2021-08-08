import socket

port = 8080

with socket.socket() as s:
    pc_name = input("Server / IP adresse name eingeben: ")


    s.connect((pc_name,port))
    print("Verbunden mit Server")

    while 1: 
        nachricht_empf=s.recv(1024)
        print(":: ", nachricht_empf.decode())

        nachricht= input(">>")
        s.sendall(nachricht.encode())