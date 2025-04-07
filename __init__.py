from flask import Flask

app = Flask(__name__)

@app.route('/<int:n>')
def calcul_somme(n):
    somme = 0
    resultat = []
    
    for nombre in range(1, n + 1):
        if nombre % 11 == 0:
            continue
        
        if nombre % 5 == 0 or nombre % 7 == 0:
            somme += nombre
            resultat.append(str(nombre))
            
            if somme > 5000:
                return (
                    f"Somme a dépassé 5000 !<br>"
                    f"Nombres ajoutés: {', '.join(resultat)}<br>"
                    f"Somme finale: {somme}"
                )
    
    return (
        f"Calcul terminé pour n={n}<br>"
        f"Nombres ajoutés: {', '.join(resultat)}<br>"
        f"Somme finale: {somme}"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0')
