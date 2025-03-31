from flask import Flask

app = Flask(__name__)

@app.route('/<int:valeur>')
def exercice(valeur):
    etoiles = ''
    for i in range(1, valeur + 1):
        etoiles += ' ' * (valeur - i) + '*' * i + '<br>'
    return etoiles

if __name__ == "__main__":
    app.run(debug=True)
