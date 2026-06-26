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


## Obtener producto por ID

@app.route('/productos/<int:codigo>', methods=['GET'])
def obtenerProductoPorId(codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return jsonify(producto)
        
    return jsonify({
        "mensaje": "Producto no encontrado"
    }), 404

##Agregar Productos

@app.post("/productos")
def agregar_producto():
    nuevo_producto = request.get_json()

    if not nuevo_producto or "nombre" not in nuevo_producto:
        return jsonify({"error": "El campo nombre es obligatorio"}), 400

    if "precio" not in nuevo_producto:
        return jsonify({"error": "El campo precio es obligatorio"}), 400

    if "stock" not in nuevo_producto:
        return jsonify({"error": "El campo stock es obligatorio"}), 400

    codigo_producto = max(productos.keys(), default=200) + 1

    nuevo_producto["codigo"] = codigo_producto
    productos[codigo_producto] = nuevo_producto

    return jsonify(nuevo_producto), 201

if __name__ == "__main__":
    app.run(debug=True)
