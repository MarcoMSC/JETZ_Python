import socket

port = 8080

with socket.socket() as s:
    ip = socket.gethostbyname(socket.gethostname())
    print("Server gestartet auf: ", ip)
    s.bind(('', port))
    s.listen(1)
    print("Server wartet auf Anfrage...")

    connection,address= s.accept()
    with connection:
        print(address, " hat sich verbunden.")
        connection.send(b"Hallo")

        while 1: 
            nachricht_empf = connection.recv(1024)
            print(":: ", nachricht_empf.decode())

            nachricht = input(">>")
            connection.send(nachricht.encode())
