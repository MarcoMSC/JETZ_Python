# Übung Youtube download

**Bei dieser Übung geht es um ein Code-Beispiel welches es erlaubt,<br>  Youtube Videos herunterzuladen und abzuspeichern.**

Für das herunterladen wird eine Bibliothek verwendet:  **youtube-dl**
https://github.com/ytdl-org/youtube-dl

Als erstes muss diese per pip installiert werden (im Terminal eingeben)

    $> pip install youtube-dl



### Consolenbefehle für youtube-dl

Listet alle verfügbaren Formate des Video/Audio auf (mit Dateigrösse am Ende):

    $> youtube-dl --list-formats https://www.youtube.com/watch?v=7E-cwdnsiow

Erzeugt eine json Datei mit allen Infos des Videos:

    $> youtube-dl --write-info-json --skip-download  https://www.youtube.com/watch?v=FHH6hIc2GyE

Download eines Videos:

    $> youtube-dl https://www.youtube.com/watch?v=FHH6hIc2GyE

Download nur Audio Datei:

    $> youtube-dl --extract-audio https://www.youtube.com/watch?v=FHH6hIc2GyE


Weitere Infos unter https://ostechnix.com/youtube-dl-tutorial-with-examples-for-beginners/ (Englisch)


## Python integration

Beispiele sind in der JupiterNotbook Datei ***Youtube-dl_Uebung.ipynb***