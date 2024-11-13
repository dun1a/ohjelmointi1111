from flask import Flask, Response, render_template
import json

app = Flask(__name__)

# http://127.0.0.1:3000/kenttä/EFHK
@app.route('/kentta/<icao>')
def hae_kentta(icao):
    try:

        tilakoodi = 200
        vastaus = {
            "Icao": 'EFHK',
            "Name": 'Helsinki Vantaa Airport',
            "Municipality": 'Helsinki',
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen icao"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)