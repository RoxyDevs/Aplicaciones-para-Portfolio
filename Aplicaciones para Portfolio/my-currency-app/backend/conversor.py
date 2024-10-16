
#Author RoxDev

import requests

#Obtener Tipos de Cambio
def obtener_tipos_de_cambio():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["rates"]

#Convertir moneda
def convertir_moneda(monto, moneda_origen, moneda_destino):
    tipos_de_cambio = obtener_tipos_de_cambio()
    if moneda_origen == "USD":
        return monto * tipos_de_cambio[moneda_destino]
    elif moneda_destino == "USD":
        return monto / tipos_de_cambio[moneda_origen]
    else:
        return monto * tipos_de_cambio[moneda_destino] /tipos_de_cambio[moneda_origen]
    
#-------------------------------------------------------------------------------------
#Calcular Comisión de Paypal

def calcular_comision_paypal(monto,moneda):
    #Simulación de comisiones de Paypal
    comision_porcentaje = 0.029
    comision_fija = 0.30
    comision = (monto * comision_porcentaje) + comision_fija
    return comision
