from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)


def wetter():
    response = requests.get("https://www.srf.ch/meteo")
    start = response.text.find('<blockquote class="report-teaser__quote blockquote__text">') + 58
    end = start + response.text[start:].find('</blockquote>')
    wetterbericht = response.text[start:end]
    return wetterbericht

def nachricht_auswerten(nachricht):
    if nachricht is None or nachricht == "":
        return " "
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


@app.route('/', methods=['Get', 'POST'])
def index():
    befehl = request.form.get("befehl")
    antwort = nachricht_auswerten(befehl)
    print(antwort)
    return render_template('index.html', antworttext=antwort)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True) 