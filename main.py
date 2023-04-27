import flask
from flask import request, jsonify
app = flask.Flask(__name__)

# Cria lista vazia para armazenar os produtos
products = []
@app.route('/', methods=['GET'])
def home():
    return 'ok'

@app.route('/products/<id>', methods=['DELETE'])
def delete_product_by_id(id):
    i = 0
    while i < len(products):
        if id == products[i]['id']:
            product = products.pop(i)
            return jsonify(product)
        i += 1
    return jsonify({"message": "Produto nao encontrado"})

# Cria a rota para atualizar o produto
@app.route('/products/<id>', methods=['PUT'])
def update_product_by_id(id):
    i = 0
    while i < len(products):
        if id == products[i]['id']:
            products[i] = request.json
            return jsonify(products[i])
        i += 1
    return jsonify({"message": "Produto nao encontrado"})

@app.route('/products', methods=['GET'])
def list_products():
    return jsonify(products)

@app.route('/products/<int:id>', methods=['GET'])
def get_product_by_id(id:int):
    for id, product in products.keys():
        if product == product["id"]:
            return jsonify(product[id])
    return jsonify({"message": "Produto nao encontrado"})

# Cria a rota para salvar o produto
@app.route('/products', methods=['POST'])
def create_product():
    body = request.json
    products.append(body)
    return jsonify(products)

app.run(port=3000)