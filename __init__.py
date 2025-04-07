from flask import Flask

app = Flask(__name__)  # Correction: __name__ au lieu de name

@app.route('/<int:valeur>')
def exercice(valeur):
    pyramide = ''
    for i in range(1, valeur + 1):
        ligne = ''
        ligne += ' ' * (valeur - i)
        for j in range(1, i + 1):
            ligne += str(j)
        for j in range(i - 1, 0, -1):
            ligne += str(j)
        pyramide += ligne + '\n'
    return f"<pre>{pyramide}</pre>"

if __name__ == "__main__":  # Correction: __name__ et __main__
    app.run(host='0.0.0.0', port=5000, debug=True)  # Ajout de host/port
