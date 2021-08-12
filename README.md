# Übung Chat: Client Server

## ChatBot Antwort Server

In dieser Übung wird der Server erweitert, dass er eine Anfrage auf das Schlüsselwort 'Zeit', 'Datum' und 'Wetter' durchsucht (auch in einem Satz) und die entsprechende Antwort zurückgibt. 

'Zeit' => aktuelle Zeit vom Server soll zurückgegeben werden <br>
'Datum' => aktuelles Datum vom Server soll zurückgegeben werden<br>
'Wetter' => auf der "www.srf.ch/meteo" wird die aktuelle Wetterprognose extrahiert und zurückgegeben<br>

<br><br><br>

### Erklärung zum Bild:

Der Server geht zuerst in den "warten auf eine Verbingungsanfrage" Modus,  
der Client kann sich dann per Anfrage mit dem Server verbinden. 

![client server socket picture](/client_server_socket.jpg)

