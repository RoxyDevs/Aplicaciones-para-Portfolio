//frontend/src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App(){
    //El código React del ejemplo anterior
    const convertir = async ()=> {
        try {
            constresponse = await axios.post('http://localhost:5000/convertir', {
                monto: monto,
                monedaOrigen: monedaOrigen,
                monedaDestino: monedaDestino
            });
            setResultadoConversion(response.data.resultado);
        } catch (error) {
            console.error(error);
        }
    };
}