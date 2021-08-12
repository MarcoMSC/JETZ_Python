import socket
from datetime import datetime

port = 8080

def nachricht_auswerten(nachricht):
    print(":: ", nachricht)
    antwort = 'ich verstehe dies leider nicht...'
    if nachricht.lower().find("zeit") != -1:
        antwort = datetime.now().strftime('%H:%M:%S')
    return antwort

with socket.socket() as s:
    ip = socket.gethostbyname(socket.gethostname())
    print("Server gestartet auf: ", ip)
    s.bind(('', port))
    s.listen(1)
    print("Server wartet auf Anfrage...")

    connection,address= s.accept()
    with connection:
        print(address, " hat sich verbunden.")
        connection.sendall(b"Hallo")

        while 1: 
            nachricht_empf = connection.recv(1024)
            antwort = nachricht_auswerten(nachricht_empf.decode())
            connection.sendall(antwort.encode())