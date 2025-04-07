from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pyramide():
    taille = 5  # Valeur par défaut
    lignes = []
    
    if request.method == 'POST':
        taille = int(request.form.get('taille', 5))
    
    # Génération de la pyramide
    for i in range(1, taille + 1):
        espaces = ' ' * (taille - i)
        partie_gauche = ''.join(str(j) for j in range(1, i + 1))
        partie_droite = ''.join(str(j) for j in range(i - 1, 0, -1))
        lignes.append(f"{espaces}{partie_gauche}{partie_droite}")
    
    return render_template('pyramide.html', lignes=lignes, taille_actuelle=taille)

if __name__ == '__main__':
    app.run()
