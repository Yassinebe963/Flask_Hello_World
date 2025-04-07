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
    
    # Créer le HTML
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pyramide de taille {taille}</title>
        <style>
            body {{ font-family: monospace; text-align: center; }}
            pre {{ margin: 0; }}
            a {{ margin: 10px; }}
        </style>
    </head>
    <body>
        <h1>Pyramide (taille {taille})</h1>
        <div id="pyramide">
            {"".join(f"<pre>{ligne}</pre>" for ligne in lignes)}
        </div>
        <div>
            {" ".join(f'<a href="/{n}">{n}</a>' for n in range(1, 11))}
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run()
