from flask import Flask, jsonify, request

app = Flask(__name__)

productos = {
    201: {"codigo":201, "nombre": "Teclado mecanico RGB", "precio": 45.00, "stock":12},
    202: {"codigo":202, "nombre": "Mouse inalambrico", "precio": 18.50, "stock":25},
    203: {"codigo":203, "nombre": "Monitor LED 24''", "precio": 165.00, "stock":8},
}

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la API de productos",
        "version":"1.0",
        "endpoints": ["/producto","/productos/<id>"]
        })
    
@app.get("/productos")
def obtener_productos():
    return jsonify(list(productos.values()))