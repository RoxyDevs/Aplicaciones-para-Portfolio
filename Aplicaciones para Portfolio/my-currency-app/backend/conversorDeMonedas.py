# backend/app.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

#Conversión de monedas y cálculo de comisión(ejemplo anterior)

# Endpoinr para convertir monedas
@app.route('/convertir', methods=['POST'])
def convertir_moneda():
    data = request.json()
    monto = request.get('monto')
    monedaOrigen = data.get('monedaOrigen').upper()
    monedaDestino = data.get('monedaDestino').upper()
    resultado = convertir_moneda(monto, monedaOrigen, monedaDestino)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)