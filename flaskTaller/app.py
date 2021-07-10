from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')



@app.route("/edificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificios/",
                     auth=('erick', '1234'))
    edificios = json.loads(r.content)['results']
    num_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
                           num_edificios=num_edificios)




@app.route("/departamentos")
def los_departamnetos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
                     auth=('erick', '1234'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append(
            {
                'nombrePropietario': d['nombreProp'],
                'costo': d['costo'],
                'cuartos': d['numCuartos'],
                'edificio': obtener_edificio(d['edificio'])
            })
    return render_template("losdepartamentos.html", datos=datos2,
                           numero=numero)

# funciones ayuda


def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=('erick', '1234'))
    nombre_edificio = json.loads(r.content)['nombre']
    return nombre_edificio
