# Übung Youtube download mit Flask

**Bei dieser Übung geht es um ein Code-Beispiel welches es erlaubt,<br>  Youtube Videos auf einer eigenen Website einzugeben und herunterzuladen.**

![JETZ Youtube-dl Vorschau](JETZ_Youtube-dl.jpg)

Für das herunterladen wird eine Bibliothek verwendet:  **youtube-dl**
https://github.com/ytdl-org/youtube-dl

Als erstes muss diese per pip installiert werden (im Terminal eingeben)

    $> pip install youtube-dl

## Python integration

Beispiele sind in der JupiterNotbook Datei ***Youtube-dl_Uebung.ipynb***

<br><br>

## Übung 1: 

Nimm die alte Übung "Simple Webserver mit Flask" als Vorlage und baue den Code so um, dass in dem Text-Eingabefeld die URL-Adresse zu einem
Youtube Video eingegeben werden kann, und beim Drücken der Taste dieses Video heruntergeladen wird.

Falls du die alte Übung nicht mehr hast, kannst du diese einfach als Vorlage clonen (in einem Terminal eingeben):

    $> git clone https://github.com/MarcoMSC/JETZ_Python.git YoutubeDownload

    $> git checkout Übung/Simple_Webserver_mit_Flask

## Übung 2:

Erweitere die Übung 1 so, dass du wählen kannst ob das Video oder nur die Audio Datei (z.B. die Musik) herunterladen wird.<br>
Dazu kannst du z.B. einen zweiten Button oder zwei RadioButtons für die Auswahl Video/Audio einfügen.