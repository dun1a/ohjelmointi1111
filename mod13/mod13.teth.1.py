from flask import Flask, Response, render_template
import json
import alkulukuteht

app = Flask(__name__)

@app.route('/')
def tehtava():
    return 'alkulukutehtävä'

# http://127.0.0.1:3000/alkuluku/31

@app.route('/alkuluku/<alkuluku>')
def alkuluku(alkuluku):
    try:
        luku = int(alkuluku)
        # laske tässä alkuluku TAI kutsu funktio toisesta tiedostosta
        alkuluku = alkulukuteht.laske(luku)

        tilakoodi = 200

        #{'Number': 31, 'isPrime':True}

        vastaus = {
            "Number": luku,
            "isPrime": alkuluku
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku alkuluku ei voida laksea "
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)