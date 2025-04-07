from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return "Ajoutez un nombre à l'URL (ex: /5)"

@app.route('/<int:taille>')
def pyramide(taille):
    # Limiter la taille à 20 pour éviter les abus
    taille = min(taille, 20)
    
    # Générer la pyramide
    lignes = []
    for i in range(1, taille + 1):
        espaces = ' ' * (taille - i)
        gauche = ''.join(map(str, range(1, i + 1)))
        droite = ''.join(map(str, range(i - 1, 0, -1)))
        lignes.append(espaces + gauche + droite)
    
   
    

if __name__ == '__main__':
    app.run()
