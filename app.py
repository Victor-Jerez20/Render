from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

GOOGLE_SCRIPT_URL = "https://script.google.com/macros/library/d/1tEExU9z6cHr_dumFU4NhK9lh6tPQyt5IfZmBQIBlyEleDSemlTGd5jlp/1"

@app.route("/datos", methods=["GET"])
def obtener_datos():
    sheet = request.args.get("sheet")
    
    if not sheet:
        return jsonify({"error": "Falta el parámetro 'sheet'"}), 400
    
    try:
        # Enviar el parámetro 'sheet' al Apps Script
        respuesta = requests.get(GOOGLE_SCRIPT_URL, params={"sheet": sheet})
        if respuesta.status_code == 200:
            return jsonify({"valor": respuesta.text})
        else:
            return jsonify({"error": "Error desde Google Script"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
