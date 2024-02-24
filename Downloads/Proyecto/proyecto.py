from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de subastas (cada subasta es un diccionario)
auctions = [
    {"id": 1, "title": "Subasta 1", "description": "Descripción de la subasta 1", "current_bid": 50},
    {"id": 2, "title": "Subasta 2", "description": "Descripción de la subasta 2", "current_bid": 30},
]

@app.route('/')
def index():
    return render_template('index.html', auctions=auctions)

@app.route('/auction/<int:auction_id>')
def auction(auction_id):
    # Busca la subasta por ID
    auction = next((a for a in auctions if a["id"] == auction_id), None)
    if auction:
        return render_template('auction.html', auction=auction)
    else:
        return "Subasta no encontrada."

if __name__ == '__main__':
    app.run(debug=True)
