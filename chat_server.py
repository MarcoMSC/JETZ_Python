import socket
from datetime import datetime
import requests

port = 8080

def wetter():
    response = requests.get("https://www.srf.ch/meteo")
    start = response.text.find('<blockquote class="report-teaser__quote blockquote__text">') + 58
    end = start + response.text[start:].find('</blockquote>')
    wetterbericht = response.text[start:end]
    return wetterbericht

def nachricht_auswerten(nachricht):
    print(":: ", nachricht)
    if nachricht.lower().find("zeit") != -1:
        antwort = datetime.now().strftime('%H:%M:%S')
    elif nachricht.lower().find("datum") != -1:
        antwort = datetime.now().strftime('%d.%m.%Y')
    elif nachricht.lower().find("wetter") != -1:
        antwort = wetter()
    else:
        antwort = 'ich verstehe dies leider nicht...'
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
