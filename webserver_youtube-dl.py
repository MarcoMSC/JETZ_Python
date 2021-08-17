from flask import Flask, render_template, request
from datetime import datetime
import requests
import youtube_dl

app = Flask(__name__)

# optionen für youtube-dl
# Datei wird als Titel.mp4 gespeichert
ydl_opts = {
    'outtmpl': '%(title)s.%(ext)s'
}


def video_herunterladen(url):
    if url is None or url == "":
        return " "
    print(":: ", url)
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except:
        return "Fehler: kein gültiger Youtube Link"

    return "Video heruntergeladen"


@app.route('/', methods=['Get', 'POST'])
def index():
    url = request.form.get("youtube_url")
    status = video_herunterladen(url)
    print(status)
    return render_template('index.html', downloadstatus=status)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)