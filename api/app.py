from flask import Flask, jsonify, render_template
from service.amazon_service import AmazonService

app = Flask(__name__)
amazon_service = AmazonService()

@app.get("/amazon/elenco")
def elenco_amazon():
    prodotti, status = amazon_service.elenco_prodotti_amazon()
    #   sempre un array
    if not isinstance(prodotti, list):
        prodotti = []
    return jsonify(prodotti)  # RESTITUISCI SOLO L’ARRAY

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/prodotto/<id_prodotto>")
def pagina_prodotto(id_prodotto):
    return render_template("prodotto.html", id_prodotto=id_prodotto)


if __name__ == "__main__":
    app.run(debug=True)
