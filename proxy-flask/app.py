from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbzwKjD78MUIWiNbHuE95a4q1tFRRpE-v25RX-WnUQlK3xMVgY-BCky-SORIPaUeVyr7/exec"

@app.route("/datos", methods=["GET"])
def obtener_datos():
    try:
        respuesta = requests.get(GOOGLE_SCRIPT_URL)
        if respuesta.status_code == 200:
            return jsonify({"valor": respuesta.text})
        else:
            return jsonify({"error": "Error desde Google Script"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)